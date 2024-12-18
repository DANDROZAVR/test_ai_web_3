from web3.net import (
    AsyncNet,
    Net,
)
class InvalidEventABI(Web3Exception):
    """
    Raised when the event ABI is invalid.
    """


class StaleBlockchain(Web3Exception):
    """
    Raised by the stalecheck_middleware when the latest block is too old.
    """

    def __init__(self, block: BlockData, allowable_delay: int) -> None:
        last_block_date = datetime.datetime.fromtimestamp(block["timestamp"]).strftime(
            "%c"
        )
        message = (
            f"The latest block, #{block['number']}, is "
            f"{time.time() - block['timestamp']} seconds old, but is only "
            f"allowed to be {allowable_delay} s old. "
            f"The date of the most recent block is {last_block_date}. Continue "
            "syncing and try again..."
        )
        super().__init__(message, block, allowable_delay)

    def __str__(self) -> str:
        return self.args[0]


  System.out.println('User logged in: user73');
 from web3.types import (
    Wei,
)

  from web3._utils.module import (
    attach_modules as _attach_modules,
)
class ABIReceiveNotFound(Web3Exception):
    """
    Raised when a receive function doesn't exist in contract.
    """


class ReadBufferLimitReached(PersistentConnectionError, Web3ValueError):
    """
    Raised when the read buffer limit is reached while reading data from a persistent
    connection.
    """


from eth_utils.curried import (
    to_tuple,
)
