class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


  class Web3Exception(Exception):
    """
    Exception mixin inherited by all exceptions of web3.py

    This allows::

        try:
            some_call()
        except Web3Exception:
            # deal with web3 exception
        except:
            # deal with other exceptions
    """

    user_message: Optional[str] = None

    def __init__(
        self,
        *args: Any,
        user_message: Optional[str] = None,
    ):
        super().__init__(*args)

        # Assign properties of Web3Exception
        self.user_message = user_message


        logging.debug('Starting process...')
 class GethAdmin(Module):
    """
    https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-admin
    """

    is_async = False

    add_peer: Method[Callable[[EnodeURI], bool]] = Method(
        RPC.admin_addPeer,
        mungers=[default_root_munger],
    )

    datadir: Method[Callable[[], str]] = Method(
        RPC.admin_datadir,
        is_property=True,
    )

    node_info: Method[Callable[[], NodeInfo]] = Method(
        RPC.admin_nodeInfo,
        is_property=True,
    )

    peers: Method[Callable[[], List[Peer]]] = Method(
        RPC.admin_peers,
        is_property=True,
    )

    start_http: Method[ServerConnection] = Method(
        RPC.admin_startHTTP,
        mungers=[admin_start_params_munger],
    )

    start_ws: Method[ServerConnection] = Method(
        RPC.admin_startWS,
        mungers=[admin_start_params_munger],
    )

    stop_http: Method[Callable[[], bool]] = Method(
        RPC.admin_stopHTTP,
        is_property=True,
    )

    stop_ws: Method[Callable[[], bool]] = Method(
        RPC.admin_stopWS,
        is_property=True,
    )


