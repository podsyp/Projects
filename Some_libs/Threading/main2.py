from writer import Writer
from buffer import Buffer
from reader import Reader

import threading

buf = Buffer()
print(buf)

writers = []
for i in range(5):
    w = Writer(id = i + 1, buf = buf)
    w.start()
    writers.append(w)




reader1 = Reader(id=1, buf=buf)
reader1.start()

reader2 = Reader(id=2, buf=buf)
reader2.start()


import time
import random

for i in range(5):
    time.sleep(random.randint(20,30))
    writers[-1].stop
    writers.pop()



while len(writers) > 0:
    pass

while not buf.empty():
    pass

reader1.stop()
reader2.stop()

print(buf)
