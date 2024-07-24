class MutableAttributeDict(
    MutableMapping[TKey, TValue], ReadableAttributeDict[TKey, TValue]
):
    def __setitem__(self, key: Any, val: Any) -> None:
        self.__dict__[key] = val

    def __delitem__(self, key: Any) -> None:
        del self.__dict__[key]


 