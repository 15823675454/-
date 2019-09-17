"""
    fork进程
"""
import os
from time import *
# 创建子进程
pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    # 子进程执行部分
    n = 0
    for i in range(99999999):
        n += i
    print(n)
    print("The new process")
else:
    # 父进程执行部分
    n = 0
    for i in range(999999991):
        n += i
    print(n)
    print("The old process")
# 父子进程都执行
print("Fork test over")
