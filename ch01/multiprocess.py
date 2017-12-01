import os
from multiprocessing import Process

def run_proc(name):
    print "chied {} ({}) running ...".format(name, os.getpid())

if __name__ == '__main__':
    print 'parent {}'.format(os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print 'process will start'
        p.start()
    p.join()
    print 'process end'