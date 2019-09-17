from multiprocessing import Pool
import os
def copy_file(file,new,old):
    file_old = old + file
    file_new = new+file
    old1 = open(file_old, 'rb')
    new1 = open(file_new, 'wb')
    while True:
        data = old1.read(1024)
        # print(data)
        if not data:
            break
        new1.write(data)
def main():
    old = '/home/shilei/ZJ/并发编程/day03/'
    name = input('文件名：')
    new = '/home/shilei/ZJ/并发编程/'+name+'/'
    os.mkdir(new)
    list_old = os.listdir(old)
    # print(list_old)
    p = Pool(4)
    for file in list_old:
        p.apply_async(func=copy_file, args=(file, new, old))

    p.close()
    p.join()
if __name__ == '__main__':
    main()
