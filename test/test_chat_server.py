"""
chat room
env: python3.6
socket udp & fork exc
"""
import socket
import os, sys
# 全局变量：很多封装模块都要用或者有特定含义的变量
# 搭建网络
ADDR = ('0.0.0.0', 8888)
# 循环获取客户端请求
# 存储用户{name:address}
user = {}
def do_login(sockfd,name,addr):
    if name in user or '管理员' in name:
        sockfd.sendto('\n用户名已存在'.encode(), addr)
        return
    else:
        # 可以进入
        sockfd.sendto(b'OK', addr)
    # 通知其他人
    msg = "\n欢迎 %s 加入聊天室" % name
    for i in user:
        sockfd.sendto(msg.encode(), user[i])
    user[name] = addr # 加入字典
def do_chat(sockfd, name, msg):
    data = "\n%s:%s" % (name, msg)
    for i in user:
        if i != name:
            sockfd.sendto(data.encode(),user[i])
def do_quit(sockfd, name):
    msg = "\n%s退出了聊天室" % name
    for i in user:
        if i == name:
            sockfd.sendto("TEXT".encode(), user[i])
        sockfd.sendto(msg.encode(), user[i])
    del user[name]
def do_request(sockfd):
    while True:
        data, addr = sockfd.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        if tmp[0] == "L":
            do_login(sockfd, tmp[1], addr)
        elif tmp[0] == "C":
            do_chat(sockfd, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_quit(sockfd, tmp[1])
def main():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        # 管理员消息处理
        while True:
            msg = input('管理员：')
            msg = "C 管理员 " + msg
            sockfd.sendto(msg.encode(), ADDR)
    else:
        do_request(sockfd)


if __name__ == '__main__':
    main()



