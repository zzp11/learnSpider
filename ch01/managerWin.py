import random, time, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = Queue.Queue()
result_queue  = Queue.Queue()
queue = Queue.Queue()

class Queuemanager(BaseManager):
    pass

def get_task_queue():
    return task_queue
def get_result_queue():
    return result_queue

def win_run():
    Queuemanager.register('get_task_queue', callable = get_task_queue)
    Queuemanager.register('get_result_queue', callable = get_result_queue)

    m = Queuemanager(address=('127.0.0.1', 5000), authkey='zzp')

    m.start()
    try:
        task = m.get_task_queue()
        result = m.get_result_queue()

        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            print 'put task %s ...' %url
            task.put(url)

        print 'try get result ...'
        for i in range(10):
            print 'result is %s' % result.get(timeout=10)
    except:
        print('manager err')
    finally:
        m.shutdown()

if __name__ == "__main__":
    freeze_support()
    win_run()
