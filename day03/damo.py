from multiprocessing import Process
import time
def zs(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def Zjs(fun):
    def time_js(*args, **kwargs):
        start = time.time()
        n = fun(*args, **kwargs)
        end = time.time()
        print(n,end-start)
        return n, end-start
    return time_js
@Zjs
def js(n):
    sum1 = 0
    for i in range(2, n):
        if zs(i):
            sum1 += i
    return sum1
# sum1 = js()
# print(sum1)

# class MyProcess(Process):
#     def __init__(self,value):
#         self.value = value
#         super().__init__()
#     def time_jl(self,fun):
#         def time_js(*args, **kwargs):
#             start = time.time()
#             n = fun(*args, **kwargs)
#             end = time.time()
#             return n, end - start
#
#         return time_js
#     @time_jl
#     def fun1(self,*args, **kwargs):
#         sum1 = 0
#         for i in range(2, 50000):
#             if zs(i):
#                 sum1 += i
#         return sum1
#     @time_jl
#     def fun2(self, *args, **kwargs):
#         sum1 = 0
#         for i in range(50000, 100000):
#             if zs(i):
#                 sum1 += i
#         return sum1
#
#
#     def run(self):
#         a = self.fun1()
#         b = self.fun2()
@Zjs
def fun1(*args, **kwargs):
    sum1 = 0
    for i in range(2, 50000):
        if zs(i):
            sum1 += i
    return sum1
@Zjs
def fun2(*args, **kwargs):
    sum1 = 0
    for i in range(50000, 100001):
        if zs(i):
            sum1 += i
    return sum1
class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.prime = 0
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            if zs(i):
                self.prime += i
        print(self.prime)
@Zjs
def use4_process():
    process = []
    jobs = []
    for i in range(2,100001,25000):
        p = Prime(i, i+25000)
        process.append(p)
        p.start()
    [i.join() for i in jobs]

use4_process()


