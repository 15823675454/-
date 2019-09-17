from socket import *
# 与客户端交互

def handle(confd):
    # 获取http请求
    data = confd.recv(4096).decode()
    print('data:',data)
    request_line = data.split('\n')[0]
    print('行：',request_line)
    info = request_line.split()[1]
    # 查看请求内容是否为/
    if info == '/':
        with open('index.html') as f:
            # 组织http响应格式
            response = """HTTP/1.1 200 OK
            Content-Type:text/html


            %s
            """ % f.read()
            # response = "HTTP/1.1 200 OK\r\n"
            # response += "Content-Type:text/html\r\n"
            # response += '\r\n'
            # response += f.read()
    else:
        response = """HTTP/1.1 404 Not Found
        Content-Type:text/html

        <h1>sorry</h1>
                    """
        # response = "HTTP/1.1 404 Not Found\r\n"
        # response += "Content-Type:text/html\r\n"
        # response += '\r\n'
        # response += "<h1>Sorry...</h1>"
    confd.send(response.encode())
    # 搭建网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8888))
    sockfd.listen(5)
    while True:
        confd, addr = sockfd.accept()
        print("Conect from", addr)
        # 处理客户端请求
        handle(confd)


main()

