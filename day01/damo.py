"""
    1.tcp 细节
    * 一端断开，另一端recv立即返回空
    * 缓冲区为空recv阻塞（缓冲区，协调收发速度）
    * 粘包（tcp才有）


    2. udp
    服务器：socket->bind->recvfrom/sendto->close


    3.套接字属性
    fileno()   文件描述符
    setsockopt() 设置套接字选项
    getpeername() 获取连接套接字客户端地址

    4.struck 模块
    功能：将一组数据进行打包转换为bytes  pack()
    将字节数据解包  unpack()
    

"""