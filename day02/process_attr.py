"""
进程对象属性
"""
from multiprocessing import Process
import time
import os


def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


p = Process(target=tm, name='时间')
# 父进程子进程随之退出
p.daemon = True
p.start()
time.sleep(2)
print("名称：", p.name)
print('父进程', os.getpid())
print('PID', p.pid)

