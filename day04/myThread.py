"""
测试用例
"""
import time
from multiprocessing import Process
from threading import Thread
# 单进程时间: 5.944053411483765
# 10进程时间: 3.169448137283325
# 10线程时间: 5.8551366329193115
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1
# 单进程时间: 44.934661626815796
# 10进程时间: 18.627253770828247
# 10线程时间: 172.12680315971375
def io():
    write()
    read()
def write():
    f = open('test', 'w')
    for i in range(1700000):
        f.write("hello world")

def read():
    f = open('test', 'r')
    for i in range(1700000):
        f.read()
# start = time.time()
# for i in range(10):
#     io()
# end = time.time()
# print('单进程时间:',end-start)
start = time.time()
jobs = []
for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
end = time.time()
print('10线程时间:', end-start)


