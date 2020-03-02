from writer import Writer
from buffer import Buffer
from reader import Reader

import threading

buf = Buffer()
print(buf)

writer1 = Writer(id=1, buf= buf)
writer1.start()

writer2 = Writer(id=2, buf= buf)
writer2.start()

reader = Reader(id=1, buf=buf)
reader.start()

import time
time.sleep(30)

threading.enumerate()

writer1.stop()
writer2.stop()

while not buf.empty():
    pass

reader.stop()

print(buf)
