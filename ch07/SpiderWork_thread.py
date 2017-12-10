# coding: utf-8

from multiprocessing.managers import BaseManager
from HtmlParser import HtmlParser
import time
import threading

from HtmlDownloader import HtmlDownloader

lock = 0

class SpiderWork(object):
    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        server_addr = '127.0.0.1'
        print('connect to server %s ...' % server_addr)
        self.m = BaseManager(address=(server_addr, 8001), authkey='baike')
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()

        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

        self.lock = 0
        self.start = time.time()
        print 'init finish'

    def work_thread(self, url):
        global lock
        self.lock += 1
        print '爬虫节点正在解析：%s' % url.encode('utf-8')
        #yield
        content = self.downloader.download(url)
        new_urls, data = self.parser.parser(url, content)
        self.result.put({'new_urls': new_urls, 'data': data})
        print '爬虫节点解析完成：%s' % url.encode('utf-8')
        self.lock -= 1

    def gevent_print(self, str):
        print str

    def crawl(self):
        global lock
        while(True):
            try:
                if self.lock > 10:
                    time.sleep(1)
                elif not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        while self.lock:
                            time.sleep(0.1)
                        print '控制节点通知爬虫节点停止工作...'
                        print "using time:", time.time() - self.start
                        self.task.put('end')
                        self.result.put({'new_urls':'end', 'data':'end'})
                        return
                    thread = threading.Thread(target=self.work_thread, args = (url,))
                    thread.start()
                    #time.sleep(0.1)
            except EOFError, e:
                print "连接工作节点失败"
                return
            except Exception, e:
                print e
                print 'Crawl fali'

if __name__ == "__main__":
    spider = SpiderWork()
    spider.crawl()
