"""
进程间通信——管道(Pipe)
注意：管道对象需在父进程中创建，子进程从父进程获取
"""
from multiprocessing import Process,Pipe
# 创建管道
# False单向管道
# 不要在一个进程中同时使用fd1,fd2
fd1, fd2 = Pipe()


def app1():
    print('启动app1,请登录，（可以使用app2）')
    print('向app2发请求')
    # 写管道

    fd1.send('app1想要：用户名，头像')
    data = fd1.recv()
    if data:
        print(data, '登录成功')
    else:
        print(data, '登录失败')


def app2():
    # 读管道
    data = fd2.recv()
    print(data)
    if data:
        fd2.send({'name': 'tom', 'image': '美女'})
    else:
        fd2.send('你要啥')


list1 = [app1, app2]
job = []
for i in list1:
    p = Process(target=i)
    job.append(p)
    p.start()
for i in job:
    i.join()
