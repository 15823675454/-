"""
process_server 多进程并发

1.创建监听套接字
2.等待客户端连接
3.客户端连接创建新的进程为客户端服务
4.父进程继续等待其他客户端连接
5.客户端退出，对应的子进程也退出
"""
import os
from socket import *
from multiprocessing import Process
import signal
# from threading import Thread

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listen the port 8888...")
n = 0
while True:
    try:
        c, addr = sockfd.accept()
        print("conect from", addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    n += 1
    print(n)
    # 创建线程
    p = Process(target=handle, args=(c,))
    p.daemon = True
    p.start()





