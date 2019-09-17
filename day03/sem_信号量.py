"""
sem 信号量
注意：信号量相当于资源，多个进程对数量进行控制
"""
from multiprocessing import Process, Semaphore
from time import sleep
import os
# 创建信号量
sem = Semaphore(3)


# 任务函数
def handle():
    # 执行任务必须消耗一个信号量
    sem.acquire()
    print("开始执行任务：", os.getpid())
    sleep(2)
    print("执行任务结束:", os.getppid())
    # 增加一个信号量
    sem.release()


for i in range(10):
    p = Process(target=handle)
    p.start()
    # p.join()
