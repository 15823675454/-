from socket import *
import sys
# 服务器地址
ADDR = ("127.0.0.1", 8888)

class FtpClient:
    def __init__(self, s):
        self.s = s
    # 退出
    def do_quit(self):
        self.s.send(b"Q")
        self.s.close()
        sys.exit("客户端退出")
    # 查看文件列表
    def do_list(self):
        self.s.send(b'L')
        # 等待回复，确定是否有文件列表
        data = self.s.recv(128).decode()
        if data == 'OK':
            data = self.s.recv(1024*1024).decode()
            if data == '':
                return
            print(data.split('\n'))
            # while True:
            #     data = self.s.recv(128).decode()
            #     if data == '##':
            #         break
        else:
            print(data)
    def do_get(self,filename):
        # 发送请求
        self.s.send(('G ' + filename).encode())
        # 等待回复
        data = self.s.recv(128).decode()
        # 接收文件
        if data == 'OK':
            f = open(filename, 'wb')
            while True:
                data = self.s.recv(1024)
                if not data:
                    f.flush()
                    f.close()
                    return
                f.write(data)
                f.flush()
        else:
            print(data)
    # 获取文件
    def get_file(self,file):
        self.s.send(file.encode())
        data = self.s.recv(1024).decode()
        if data == 'OK':
            fd = open(file, 'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    return
                fd.write(data)
        else:
            print(data)
    def do_put(self,filename):
        msg = 'P '+filename
        self.s.send(msg.encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            fd = open(filename, 'rb')
            fd.seek(0)
            while True:
                data = fd.read(1024)
                if not data:
                    self.s.send(b'##')

                    break
                self.s.send(data)
            fd.close()
        else:
            print(data)
# 网络搭建，和终端输入命令选项
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except KeyboardInterrupt:
        sys.exit("客户端退出")
    except Exception as e:
        print(e)
        return
    # 实例化对象
    ftp = FtpClient(s)
    # 循环发起请求
    while True:
        print("\n===========Command============")
        print("***********     list     ********")
        print("***********   get file   ********")
        print("***********   put file   ********")
        print("***********     quit     ********")
        print("=================================")
        cmd = input("输入：")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        # elif cmd[:3] == 'get':
        #     filename = cmd.split(' ')[-1]
        #     ftp.do_get(filename)
        elif cmd.split()[0] == 'get':
            msg = 'G '+cmd.split(' ')[1]
            ftp.get_file(msg)
        elif cmd.split()[0] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()


