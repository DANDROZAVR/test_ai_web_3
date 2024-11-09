class MethodNotSupported(Web3Exception):
    """
    Raised when a method is not supported by the provider.
    """


class ContractPanicError(ContractLogicError):
    """
    Raised when a contract reverts with Panic, as of Solidity 0.8.0
    """


from web3._utils.module import (
    attach_modules as _attach_modules,
)
from eth_typing.evm import (
    ChecksumAddress,
)

