
class BufferException(BaseException):
    _code = None
    _message = None

    def __init__(self, code: int = 0, msg: str = ''):
        self._code = code
        self._message = msg

    def getCode(self)->int:
        return self._code

    def getMessage(self)->int:
        return self._message