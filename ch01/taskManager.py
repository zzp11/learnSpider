import random, time, Queue
from multiprocessing.manager import BaseManager

task_queue = Queue.Queue()
result_queue  = Queue.Queue()

class Queuemanager(BaseManager):
    pass

Queuemanager.register('get_task_queue', callable = lambda : task_queue)
Queuemanager.register('get_result_queue', callable = lambda : result_queue)