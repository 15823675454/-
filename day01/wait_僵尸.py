"""
    处理僵尸进程
"""
import os
pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print("Child process", os.getpid())
    os._exit(1) #进程退出
else:
    # 阻塞等待回收子进程
    pid, status = os.wait()
    print("pid:", pid)
    print("status:", status)
    while True: # 让父进程不退出
        pass
