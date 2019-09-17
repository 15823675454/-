from multiprocessing import Process
import time
file = open('/home/shilei/ZJ/并发编程/day02/timg.jpeg', 'rb')
data = file.readlines()
def front(data):
    # time.sleep(1)
    file1 = open('front.jpeg', 'wb')
    for i in range(len(data)//2):
        file1.write(data[i])
        file1.flush()
    file1.close()
def end(data):
    file2 = open('end.jpeg', 'wb')
    for i in range(len(data)//2, len(data)):
        file2.write(data[i])
        file2.flush()
    file2.close()
list1 = [front, end]
jobs = []
for i in list1:
    p = Process(target=i, kwargs={'data': data})
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
