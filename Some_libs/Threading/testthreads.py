import _thread

number_threads = 0

def checkPrimary(n: int)->bool:
    import math
    q = int(math.sqrt(n))
    for i in range(2, q):
        if n % i ==0:
            return False
    return True

def fillPrimaryNumber(ls: list, count: int):
    global number_threads
    global mut1
    global mut2

    mut1.acquire()
    number_threads = number_threads + 1
    mut1.release()

    import random
    while True:
        e = random.randint(10 ** 11, 10 ** 14)
        if checkPrimary(e):
            mut2.acquire()
            if len(ls) >= count:
                mut2.release()
                break
            if (not e in ls):
                ls.append(e)
            mut2.release()

    mut1.acquire()
    number_threads = number_threads - 1
    mut1.release()

ls = []

mut1 = _thread.allocate_lock()
mut2 = _thread.allocate_lock()

thread1 = _thread.start_new(fillPrimaryNumber, (ls, 8))
thread2 = _thread.start_new(fillPrimaryNumber, (ls, 8))

import time
time.sleep(1)

while number_threads > 0:
    time.sleep(1)

print(ls)
print(len(ls))
