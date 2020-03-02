import threading
from buffer import Buffer
from myexception import BufferException


class Writer(threading.Thread):
    _buffer = None
    _is_run = True
    _id = 0

    def __init__(self, id: int, buf: Buffer):
        threading.Thread.__init__(self)
        self._buffer = buf
        self._id = id

    def _createdRandomString(self, size: int)->str:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''
        import random
        for i in range(size):
            s += random.choice(alphabet)

        return s

    def run(self):
        import time
        import random

        while self._is_run:
            size = random.randint(20, 50)
            s = self._createdRandomString(size)
            try:
                self._buffer.write(self._id, s)
            except BufferException as err:
                print('Error:' + str(err.getCode()) + ' : ' + err.getMessage())
                time.sleep(10)
            time.sleep(random.randint(2, 7))

    def stop(self):
        self._is_run = False
        print("worker id " + str(self._id) + ' stop')

