"""
chat room 客户端
发送请求，展示结果
"""
import socket
import os,sys
# 服务器地址
ADDR = ('127.0.0.1', 8888)
def do_send(sockfd, name):
    while True:
        try:
            text = input('\n发送：')
        except (KeyboardInterrupt, SyntaxError):
            text = 'exit'
        if text == 'exit':
            msg = "Q %s %s\n" % (name, text)
            sockfd.sendto(msg.encode(), ADDR)
            sys.exit()
        msg = "C %s %s\n" % (name, text)
        sockfd.sendto(msg.encode(), ADDR)
def do_recv(sockfd):
    while True:
        data, addr = sockfd.recvfrom(1024)
        if data.decode() == "TEXT":
            sys.exit("退出聊天室")
        print(data.decode())
# 搭建网络
def main():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        name = input('请输入用户名：')
        msg = "L " + name
        sockfd.sendto(msg.encode(), ADDR)
        # 接受反馈
        data, addr = sockfd.recvfrom(128)
        if data == b'OK':
            print('您已进入聊天室')
            break
        else:
            print(data.decode())
    pid = os.fork()
    if pid == 0:
        do_send(sockfd, name)
    else:
        do_recv(sockfd)

if __name__ == '__main__':
    main()

