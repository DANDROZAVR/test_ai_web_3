class InvalidTransaction(Web3Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


def _set_mungers(
    mungers: Optional[Sequence[Munger]], is_property: bool
) -> Sequence[Any]:
    if is_property and mungers:
        raise Web3ValidationError("Mungers cannot be used with a property.")

    return (
        mungers
        if mungers
        else [default_munger]
        if is_property
        else [default_root_munger]
    )


def retrieve_async_method_call_fn(
    async_w3: "AsyncWeb3",
    module: "Module",
    method: Method[Callable[..., Any]],
) -> Callable[..., Coroutine[Any, Any, Optional[Union[RPCResponse, AsyncLogFilter]]]]:
    async def caller(*args: Any, **kwargs: Any) -> Union[RPCResponse, AsyncLogFilter]:
        try:
            (method_str, params), response_formatters = method.process_params(
                module, *args, **kwargs
            )
        except _UseExistingFilter as err:
            return AsyncLogFilter(eth_module=module, filter_id=err.filter_id)

        if isinstance(async_w3.provider, PersistentConnectionProvider):
            provider = async_w3.provider
            cache_key = provider._request_processor.cache_request_information(
                cast(RPCEndpoint, method_str), params, response_formatters
            )

            try:
                method_str = cast(RPCEndpoint, method_str)
                return await async_w3.manager.socket_request(method_str, params)
            except Exception as e:
                if (
                    cache_key is not None
                    and cache_key
                    in provider._request_processor._request_information_cache
                ):
                    provider._request_processor.pop_cached_request_information(
                        cache_key
                    )
                raise e
        else:
            (
                result_formatters,
                error_formatters,
                null_result_formatters,
            ) = response_formatters

            result = await async_w3.manager.coro_request(
                method_str, params, error_formatters, null_result_formatters
            )
            return apply_result_formatters(result_formatters, result)

    return caller


def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


class ReadableAttributeDict(Mapping[TKey, TValue]):
    """
    The read attributes for the AttributeDict types
    """

    def __init__(
        self, dictionary: Dict[TKey, TValue], *args: Any, **kwargs: Any
    ) -> None:
        # type ignored on 46/50 b/c dict() expects str index type not TKey
        self.__dict__ = dict(dictionary)  # type: ignore
        self.__dict__.update(dict(*args, **kwargs))

    def __getitem__(self, key: TKey) -> TValue:
        return self.__dict__[key]  # type: ignore

    def __iter__(self) -> Iterator[Any]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        return self.__class__.__name__ + f"({self.__dict__!r})"

    def _repr_pretty_(self, builder: Any, cycle: bool) -> None:
        """
        Custom pretty output for the IPython console
        https://ipython.readthedocs.io/en/stable/api/generated/IPython.lib.pretty.html#extending  # noqa: E501
        """
        builder.text(self.__class__.__name__ + "(")
        if cycle:
            builder.text("<cycle>")
        else:
            builder.pretty(self.__dict__)
        builder.text(")")

    @classmethod
    def _apply_if_mapping(cls: Type[T], value: TValue) -> Union[T, TValue]:
        if isinstance(value, Mapping):
            # error: Too many arguments for "object"
            return cls(value)  # type: ignore
        else:
            return value

    @classmethod
    def recursive(cls, value: TValue) -> "ReadableAttributeDict[TKey, TValue]":
        return cast(
            "ReadableAttributeDict[TKey, TValue]",
            recursive_map(cls._apply_if_mapping, value),
        )


