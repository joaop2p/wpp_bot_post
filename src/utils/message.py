class Message:
    _message: str
    _message_type: str

    def __init__(self, message: str, message_type: str) -> None:
        self._message = message
        self._message_type = message_type

    @property
    def getMessage(self) -> str:
        return self._message
    @property
    def getMessage_type(self) -> str:
        return self._message_type