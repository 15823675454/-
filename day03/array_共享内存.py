"""
array 存放一组数据
"""
from multiprocessing import Process,Array
# 共享内存，初始[1, 2, 3, 4, 5]
# shm = Array('i', [1, 2, 3, 4, 5])
# shm = Array('i', 4)# 共享内存，初始[0,0,0,0]
shm = Array('c', b'hello')

def fun():
    # 迭代获取共享内存
    for i in shm:
        print('子进程：', i)
    shm[0] = b'H'


p = Process(target=fun)
p.start()
p.join()
print(shm.value) # 只能打印共享内存的字节串
# for i in shm:
#     print('父进程：', i)


