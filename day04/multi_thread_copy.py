"""
模拟开启多个线程，在多资源情况下共同下载一个文件
"""
import os
from threading import Thread,Lock
urls = ["/home/shilei/桌面/",
        "/home/shilei/视频/",
        "/home/shilei/图片/",
        "/home/shilei/下载/",
        "/home/shilei/音乐/",
        "/home/shilei/文档/",
        "/home/shilei/模板/",
        "/home/shilei/公共/"]
lock = Lock()
filename = input("输入下载的文件名：")
explorer = []
for i in urls:
    # 判断资源库路径中文件是否存在
    if os.path.exists(i+filename):
        # 存储文件路径
        explorer.append(i+filename)
num = len(explorer) # 获取有多少资源
if num == 0:
    print('没有资源')
    os._exit(0)
size = os.path.getsize(explorer[0])
block_size = size//num + 1
fd = open(filename, 'wb')

# print(explorer,block_size)
def load(path, number):
    file = open(path, 'rb') # 从资源读取内容
    seek_types = block_size * number
    file.seek(seek_types)
    size = block_size
    # data = file.read(block_size)
    lock.acquire()
    fd.seek(seek_types)
    while True:
        if size < 1024:
            data = file.read(size)
            fd.write(data)
            fd.flush()
            break
        else:
            data = file.read(1024)
            fd.write(data)
            fd.flush()
            size -= 1024
    lock.release()

n = 0 # 给每个线程分配的是第几块
jobs = []
for path in explorer:
    t = Thread(target=load, args=(path, n))
    jobs.append(t)
    t.start()
    n += 1

for i in jobs:
    i.join()






