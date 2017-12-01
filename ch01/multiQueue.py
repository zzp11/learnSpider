from multiprocessing import Process, Queue
import os, time, random

def proc_write(q, urls):
    print 'process {} is writing...'.format(os.getpid())
    for url in urls:
        q.put(url)
        print 'put {} to queue...'.format(url)
        time.sleep(random.random())

def proc_read(q):
    print 'process {} is reading ...'.format(os.getpid())
    while True:
        url = q.get(True)
        print 'get {} from queue.'.format(url)

if __name__ == '__main__':
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))

    proc_write1.start()
    proc_write2.start()

    proc_reader.start()

    proc_write1.join()
    proc_write2.join()
    proc_reader.terminate()

