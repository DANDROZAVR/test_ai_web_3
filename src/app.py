class MethodNotSupported(Web3Exception):
    """
    Raised when a method is not supported by the provider.
    """


class ContractPanicError(ContractLogicError):
    """
    Raised when a contract reverts with Panic, as of Solidity 0.8.0
    """


print('Configuration updated')
print('Ending process...')
logging.debug('Ending process...')
