"""
ftp
"""
from socket import *
from threading import Thread
import sys,os
from time import sleep
FTP = '/home/shilei/FTP/'
# 具体功能实现
class FtpServer(Thread):
    """
    实现具体功能请求
    """
    def __init__(self, connfd):
        self.connfd = connfd

        super().__init__()
    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("请充值!".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            filelist = ""
            for file in files:
                if file[0] != '.' and os.path.isfile(FTP + file):
                 filelist += file + '\n'
            self.connfd.send(filelist.encode())
        # for file in files:
        #     # 不是隐藏文件 并且是普通文件
        #     if file[0] != '.' and os.path.isfile(FTP+file):
        #         self.connfd.send(file.encode())
        # self.connfd.send('##'.encode())
    def do_file(self,file):
        if file in os.listdir(FTP):
            self.connfd.send(b'OK')
            sleep(0.1)
            filed = open(FTP+file, 'rb')
            filed.seek(0)
            while True:
                data = filed.read(1024)
                if not data:
                    sleep(0.1)
                    self.connfd.send(b'##')
                    break
                else:
                    self.connfd.send(data)
            filed.close()
        else:
            self.connfd.send('该文件不存在'.encode())
    def do_put(self,filename):
        filename = filename.split('/')[-1]
        if filename in os.listdir(FTP):
            self.connfd.send('该文件已存在'.encode())
        else:
            self.connfd.send('OK'.encode())
            sleep(0.1)
            fd = open(FTP+filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
                fd.flush()
            fd.close()


    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # 判断请求类型
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data.split(' ')[0] == 'G':
                self.do_file(data.split(' ')[-1])
            elif data.split()[0] == 'P':
                self.do_put(data.split()[-1])
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

