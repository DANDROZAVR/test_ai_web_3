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
