"""
    multiprocessing 模块创建进程
    1.编写进程执行函数
    2.创建进程对象
    3.启动进程
    4.回收进程
"""
import multiprocessing as mp
from time import sleep

a = 1
# 进程函数
def fun1():
    print('进程1')
    sleep(3)
    print('子a:', a)
    print("进程1结束")


# 创建进程对象
p = mp.Process(target=fun1)
# 启动进程
p.start()

print('父进程')
# 回收进程
p.join()


