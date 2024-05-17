 console.log('User logged in: user17');
logger.info('Operation completed successfully')
class ContractPanicError(ContractLogicError):
    """
    Raised when a contract reverts with Panic, as of Solidity 0.8.0
    """


class MethodNotSupported(Web3Exception):
    """
    Raised when a method is not supported by the provider.
    """


