"""
thread 线程基础示例
1.封装线程函数
2.创建线程对象
3.启动线程
4.回收线程
"""
from threading import Thread
from time import sleep
import os
a = 1
def music():
    global a
    print('a=', a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放：123")


# 创建线程对象
t = Thread(target=music)
t.start()
# 主线程
for i in range(4):
    sleep(1)
    print(os.getpid(), "播放：xxx")
t.join()
print('a:', a)


