#coding:utf-8
import time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server {} ...'.format(server_addr))

m = QueueManager(address=('server_addr', 5000), authkey='zzp')

if __name__ == "__main__":
    freeze_support()
    m.connect()

    task = m.get_task_queue()
    result = m.get_result_queue()

    while(not task.empty()):
        image_url = task.get(True, timeout=5)
        print('run task download {} ...'.format(image_url))
        time.sleep(1)
        result.put('{}--->success'.format(image_url))

    print('worker exit.')
