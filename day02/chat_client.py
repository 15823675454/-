"""
chat room 客户端
发送请求，展示结果
"""
import socket
import os,sys




# 服务器地址
ADDR = ('127.0.0.1', 8888)
def send_msg(sockfd, name):
    while True:
        try:
            text = input('\n发送：')
        except (KeyboardInterrupt, SyntaxError):
            text = 'quit'
        if text.strip() == "quit":
            msg = "Q " + name
            sockfd.sendto(msg.encode(), ADDR)
            sys.exit("\n退出聊天室")
        msg = "C %s %s" % (name, text)
        sockfd.sendto(msg.encode(), ADDR)
def recv_msg(sockfd):
    while True:
        data, addr = sockfd.recvfrom(4069)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode()+'\n输入：', end='')
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
    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(sockfd, name)
    else:
        recv_msg(sockfd)
        # while True:
        #     msg = input('请输入发送消息：').encode()
        #     user_data = struct.pack('s', name, msg)
        #     sockfd.sendto(user_data, ADDR)
        #     data = sockfd.recvfrom(1024)
        #     print(data)



if __name__ == '__main__':
    main()

