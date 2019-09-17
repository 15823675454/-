from socket import *
import sys
# 服务器地址
ADDR = ("127.0.0.1", 8888)

class FtpClient:
    def __init__(self, s):
        self.s = s
    # 查看
    def do_look(self):
        self.s.send(b'L')
        while True:
            data = self.s.recv(1024).decode()
            if data == '##':
                break
            print(data)

        # print('显示完毕')
    # 退出
    def do_quit(self):
        self.s.send(b"Q")
        self.s.close()
        sys.exit("客户端退出")

    def do_get(self, filename):
        self.s.send(('G '+filename).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
                fd.flush()
            fd.close()

    def do_put(self, filename):
        self.s.send(('P '+filename.split('/')[-1]).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            fd = open(filename, 'rb')
            fd.seek(0)
            while True:
                data = fd.readline()
                if not data:
                    break
                self.s.send(data)
            fd.close()


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
            ftp.do_look()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            ftp.do_get(cmd.split(' ')[-1])
        elif cmd[:3] == 'put':
            ftp.do_put(cmd.split(' ')[-1])
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()


