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


