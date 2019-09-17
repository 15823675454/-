"""
queue 消息队列
注意：通过一个对象操作队列，满足先进先出原则
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint
# 创建消息队列
q = Queue(5)
# 请求进程
def request():
    for i in range(10):
        sleep(0.5)
        t = (randint(1, 100), randint(1, 100))
        q.put(t)
        print("===============")


# 数据处理进程
def handle():
    while True:
        sleep(2)
        x, y = q.get()
        print("数据处理结果 %s + %s = " % (x, y), x + y)

list1 = [request, handle]
job = []
for i in list1:
    p = Process(target=i)
    job.append(p)
    p.start()
for i in job:
    i.join()

