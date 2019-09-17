"""
同时创建多个子进程
"""
import multiprocessing as mp
from time import sleep
import os
def fun1():
    sleep(3)
    print('进程1吃饭')
    print(os.getppid(), '--', os.getpid())
def fun2():
    sleep(2)
    print('进程2睡觉')
    print(os.getppid(), '--', os.getpid())
def fun3():
    sleep(4)
    print('进程3打豆豆')
    print(os.getppid(), '--', os.getpid())
list01 = [fun1, fun2, fun3]
jobs = []
for i in list01:
    p = mp.Process(target=i)
    # 列表存储进程对象
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
