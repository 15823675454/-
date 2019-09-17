"""
block_io  非阻塞io
"""
from socket import *
from time import *
import sys
s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(5)
# 设置套接字非阻塞
# s.setblocking(False)
# 设置超时时间
s.settimeout(3)
f = open('log.txt', 'a')
while True:
    try:
        c, addr = s.accept()
        print("connect from", addr)
    except (BlockingIOError, timeout) as B:
        sleep(2)
        f.write(ctime()+':'+str(B)+'\n')
        f.flush()
    except KeyboardInterrupt:
        sys.exit("退出成功")
    else:
        data = c.recv(1024)
        print(data.decode())
