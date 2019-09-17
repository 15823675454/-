"""
ftp
"""
from socket import *
from threading import Thread
import sys, os
from time import sleep
# 具体功能实现
path = '/home/shilei/FTP/'
class FtpServer(Thread):
    """
    实现具体功能请求
    """
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()
        self.list_dir = os.listdir(path)
    def do_list(self):
        for i in self.list_dir:
            sleep(0.1)
            self.connfd.send(i.encode())
        sleep(0.2)
        self.connfd.send(b'##')
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # 判断请求类型
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data.split(' ')[0] == 'G':
                self.do_get(data.split(' ')[-1])
            elif data.split(' ')[0] == 'P':
                self.do_put(data.split(' ')[-1])
    def do_get(self, filename):
        if filename in self.list_dir:
            self.connfd.send(b'OK')
            data = open(path+filename, 'rb')
            data.seek(0)
            while True:
                text = data.readline()
                if not text:
                    break
                self.connfd.send(text)
            data.close()
            sleep(0.1)
            self.connfd.send(b'##')
        else:
            self.connfd.send('该文件不存在'.encode())

    def do_put(self, filename):
        if filename in self.list_dir:
            self.connfd.send('该文件已存在'.encode())
        else:
            self.connfd.send('OK'.encode())
            fd = open(path+filename,'wb')
            while True:
                data = self.connfd.recv(1024)
                if not data:
                    break
                fd.write(data)
                fd.flush()
            fd.close()
# 搭建网络并发模型
def main():
    sockfd = socket()
    ADDR = ("0.0.0.0", 8888)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    while True:
        try:
            c, addr = sockfd.accept()
            print("conect from", addr)
        except KeyboardInterrupt as e:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        t = FtpServer(c)
        t.setDaemon(True)
        t.start()
if __name__ == '__main__':
    main()

