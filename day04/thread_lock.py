"""
线程锁 lock
"""
from threading import Lock,Thread
a = b = 0
lock = Lock()
def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print('a:%d,b:%d'%(a, b))

        lock.release() # 解锁
t = Thread(target=value)
t.start()
while True:
    with lock:# 上锁
        a += 1
        b += 1

        # 解锁
t.join()

