"""
event 线程互斥
"""
from threading import Event,Thread
s = None
e = Event()
def 杨子荣():
    global s
    s = '天王盖地虎'
    e.set()
t = Thread(target=杨子荣)
t.start()
e.wait()
if s == '天王盖地虎':
    print('进山门')
else:
    print('打死他')
t.join()






