"""
value 开辟共享内存
注意：共享内存只能有一个值
"""
from multiprocessing import Process,Value
import time
from random import randint
# 创建共享内存
money = Value('i', 5000)


# 操作内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100, 800)


p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()
print("一个月后：", money.value)
