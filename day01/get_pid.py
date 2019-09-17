"""
    获取进程pid
"""
import os
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child pid:", os.getpid())
    print("Get parent PID", os.getppid())
else:
    print("parent pid :", os.getpid())
    print("get child pid:", pid)


