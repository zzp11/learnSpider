from multiprocessing import Pool
import os, time, random

def run_task(name):
    print 'task {} (pid = {}) is running ...'.format(name, os.getpid())
    time.sleep(random.random() * 3)
    print 'task {} end.'.format(name)

if __name__ == '__main__':
    print "process {}".format(os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args = (i,))
    print 'waiting for all sub processes done...'
    p.close()
    p.join()
    print "all subprocesses done."
