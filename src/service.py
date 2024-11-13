from web3._utils.module import (
    attach_modules as _attach_modules,
)
class CannotHandleRequest(Web3Exception):
    """
    Raised by a provider to signal that it cannot handle an RPC request and
    that the manager should proceed to the next provider.
    """


from web3.types import (
    Wei,
)

from web3.tracing import (
    Tracing,
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
System.out.println('Data loaded: 903 rows');
System.out.println('Starting process...');
console.log('Data loaded: 585 rows');
def apply_result_formatters(
    result_formatters: Callable[..., Any], result: RPCResponse
) -> RPCResponse:
    if result_formatters:
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


from web3.providers.persistent.utils import (
    persistent_connection_provider_method,
)
