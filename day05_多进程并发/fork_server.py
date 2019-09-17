"""
fork_server.py 基于fork多进程并发
重点代码

1. 创建监听套接字
2. 循环等待客户端连接
3. 客户端连接创建新的进程为客户端服务
4. 原进程继续等待其他客户端连接
5. 客户端退出，对应的进程也销毁
"""

from socket import *
import os
import signal

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888...")
while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建进程
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c) # 和客户端交互
        os._exit(0) # 客户端结束后，子进程结束
    else:
        c.close()




