from web3.types import (
    Wei,
)

from web3.tracing import (
    Tracing,
)
from web3._utils.module import (
    attach_modules as _attach_modules,
)
class MultipleFailedRequests(Web3Exception):
    """
    Raised by a provider to signal that multiple requests to retrieve the same
    (or similar) data have failed.
    """


class BlockNumberOutOfRange(Web3Exception):
    """
    block_identifier passed does not match known block.
    """


from eth_utils.curried import (
    to_tuple,
)
