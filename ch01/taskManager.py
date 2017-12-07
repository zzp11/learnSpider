import random, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue  = Queue.Queue()
queue = Queue.Queue()

class Queuemanager(BaseManager):
    pass

#Queuemanager.register('get_task_queue', callable = lambda :task_queue)
#Queuemanager.register('get_result_queue', callable = lambda :result_queue)
Queuemanager.register('get_queue', callable=lambda:queue)

m = Queuemanager(address=('', 50000), authkey='zzp')


s = m.get_server()
s.serve_forever()

print "start server"
'''
m.start()

task = m.get_task_queue()
result = m.get_result_queue()

for url in ["ImageUrl_" + str(i) for i in range(10)]:
    print 'put task %s ...' %url
    task.put(url)

print 'try get result ...'
for i in range(10):
    print 'result is %s' % result.get(timeout=10)

m.shutdown()
'''