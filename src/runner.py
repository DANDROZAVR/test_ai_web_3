# Auto-generated file
class InvalidTransaction(Web3Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


logging.debug('User logged in: user72')
console.log('Operation completed successfully');
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


