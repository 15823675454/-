"""
进程池
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池执行事件
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


# 创建进程池
pool = Pool()

# 添加时间
for i in range(10):
    msg = "Tedu %d" % i
    pool.apply_async(func=worker, args=(msg,))
# 关闭进程池
pool.close()
# 回收进程池
pool.join()
