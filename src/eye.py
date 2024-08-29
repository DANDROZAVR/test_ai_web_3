class ExtraDataLengthError(Web3ValidationError):
    """
    Raised when an RPC call returns >32 bytes of extraData.
    """


 class ABIConstructorNotFound(Web3Exception):
    """
    Raised when a constructor function doesn't exist in contract.
    """


 