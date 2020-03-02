from myexception import BufferException
import threading

class Buffer:

    _ls_tuple = None
    _mut = None

    def __init__(self):
        self._ls_tuple = []
        self._mut = threading.Lock() #Объект блокировки

    def write(self, id: int, msg: str):
        self._mut.acquire()
        if len(self._ls_tuple) <= 5:
            self._ls_tuple.append((id, msg, ))
        else:

            self._mut.release()
            raise BufferException(100, 'Full Buffer')
        self._mut.release()

    def read(self)->tuple:
        rec = None
        self._mut.acquire()
        if len(self._ls_tuple) > 0:
            rec = self._ls_tuple[0]
            del(self._ls_tuple[0])
            self._mut.release()
        else:
            self._mut.release()
            raise BufferException(code=10, msg='Empty Buffer')

        return rec

    def __str__(self):
        return self._ls_tuple.__str__()

    def empty(self)->bool:
        return len(self._ls_tuple) == 0