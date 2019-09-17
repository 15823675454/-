'''
    http请求响应
'''
from socket import *
sockfd = socket(AF_INET, SOCK_STREAM)
# 端口立即重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)
confd, addr = sockfd.accept()
print('地址:', addr)
data = confd.recv(4096).decode()
data = data.split()[1]
if data == '/':
    file = open('index.html', 'r')
    html = """HTTP/1.1 / 200 OK
    Content-Type:text/html

    %s
    """ % file.read()
    confd.send(html.encode())
else:
    html = """HTTP/1.1 404 NOT
        Content-Type:text/html

        NOT FOUND
        """
    confd.send(html.encode())
# html = """HTTP/1.1 200 OK
# Content-Type: text/html
#
# <h1>hello world</h1>"""


confd.close()
sockfd.close()

