from .message import Message


class Item(Message):
    post: str
    process: int
    numbers: tuple[int]
    ind_proc: str

    def __init__(self, post: str, message: str, process: int, numbers: tuple[int], ind_proc: str, dtype: str) -> None:
        self.post = post
        self.numbers = numbers
        self.process = process
        self.ind_proc = ind_proc
        Message.__init__(self, message=message, message_type=dtype)
        
    @property
    def getPost(self) -> str:
        return self.post

    @property
    def getProcess(self) -> int:
        return self.process

    @property
    def getIndProc(self) -> str:
        return self.ind_proc

    @property
    def getNumbers(self) -> tuple[int]:
        return self.numbers

    @property
    def ready(self) -> bool:
        for attr in vars(self):
            if getattr(self, attr) is None:
                return False
        return True 