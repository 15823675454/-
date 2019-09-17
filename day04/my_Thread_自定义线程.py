"""
自定义线程
"""
from threading import Thread
from time import sleep,ctime
class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs=None):
        super().__init__()
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
    def fun1(self):
        print("线程1")
    def fun2(self):
        print("线程2")
    def run(self):
        self.target(*self.args, **self.kwargs)
# 测试函数，该函数名称，参数都不确定。本函数只提供测试
def player(sec, song):
    for i in range(3):
        print("playing %s: %s" % (song, ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={"song": '凉凉'} )
t.start()
t.join()







