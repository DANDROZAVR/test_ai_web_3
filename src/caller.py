class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


 from web3._utils.rpc_abi import (
    RPC,
)
 class ContractCustomError(ContractLogicError):
    """
    Raised on a contract revert custom error
    """


class TaskNotRunning(Web3Exception):
    """
    Used to signal between asyncio contexts that a task that is being awaited
    is not currently running.
    """

    def __init__(
        self, task: "asyncio.Task[Any]", message: Optional[str] = None
    ) -> None:
        self.task = task
        if message is None:
            message = f"Task {task} is not running."
        self.message = message
        super().__init__(message)


def apply_result_formatters(
    result_formatters: Callable[..., Any], result: RPCResponse
) -> RPCResponse:
    if result_formatters:
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


