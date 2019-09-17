"""
gevent 协程模块示例
"""
import gevent
from gevent import monkey
# 导入脚本执行time模块
monkey.patch_time()
from time import sleep
# 协程函数
def foo(a, b):
    print("Running foo ..", a, b)
    # gevent.sleep(3)
    sleep(3)
    print("FOo again")
def bar(a, b):
    print("Running bar ..", a, b)
    # gevent.sleep(2)
    sleep(2)
    print("Bar again")

# 生成携程对象
f = gevent.spawn(foo, 1, 2)
g = gevent.spawn(bar, 1, 2)
# sleep(2)
gevent.joinall([f, g]) # 阻塞等待f执行完







