"""
    fork进程
"""
import os
from time import sleep
a = 1
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print('a=', a) # 从父进程空间获取的a
    print("child process")
    a = 100 # 修改自己空间的a
else:
    sleep(0.1)
    print("parent process")
    print('a:', a)
print('all_a:', a)

