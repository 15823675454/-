'''
    tcp 套接字客户端流程
    注意：和服务端配合使用同样的套接字
'''
import socket
while True:
# 创建tcp套接字
    sockfd = socket.socket()
    # 连接服务器
    server_addr = ('176.221.13.63', 8888)
    sockfd.connect(server_addr)
    # msg = input('请输入发送内容：')
    sockfd.send('1'.encode())
    n = 0
    data = sockfd.recv(1024)
    n += 1
    print(n)
    print(data)








