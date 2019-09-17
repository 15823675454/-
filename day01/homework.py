import os
pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    pid = os.fork()
    if pid < 0:
        print("child Error")
    elif pid == 0:
        print("child prosess")
    else:
        os._exit(1)
else:
    os.wait()
    print("parent process:", os.getpid())


