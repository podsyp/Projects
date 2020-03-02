import threading
from buffer import Buffer
from myexception import BufferException

class Reader(threading.Thread):
    _buf = None
    _id = 0
    _is_run = True

    def __init__(self, id: int, buf: Buffer):
        threading.Thread.__init__(self)
        self._buf = buf
        self._id = id

    def stop(self):
        self._is_run = False

    def run(self):
        import time
        import random
        while self._is_run:
            try:
                msg = self._buf.read()
                print('Reader' + str(self._id) + ' : ' + msg[1] + ' From writers ' + str(msg[0]))
            except BufferException as err:
                print('error ' + str(err.getCode()) + ' ' + err.getMessage())
            time.sleep(random.randint(1, 4))
