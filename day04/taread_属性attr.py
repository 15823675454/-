"""
thread_attr
线程属性
"""
from threading import Thread
from time import sleep
def fun():
    sleep(3)
    print('进程属性设置')
t = Thread(target=fun,name='abc')
t.setDaemon(True) # 主线程退出分支线程也退出
t.start()
t.setName('新设置的')
print("name:", t.getName())
print("is alive", t.is_alive())
print("is daemon", t.isDaemon())

# t.join()