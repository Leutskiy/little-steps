class NotSupportedException(Exception):
    """
    docstring
    """
    def __init__(self, message: str) -> None:
        super().__init__()

        self.message = message
