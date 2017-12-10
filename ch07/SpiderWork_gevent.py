# coding: utf-8

from multiprocessing.managers import BaseManager
from HtmlParser import HtmlParser
import time

from HtmlDownloader import HtmlDownloader

import gevent
from gevent import monkey;#monkey.patch_all()

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
        print 'init finish'

    def work_gevent(self, url):
        monkey.patch_all()
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
        while(True):
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        while self.lock:
                            time.sleep(0.1)
                        print '控制节点通知爬虫节点停止工作...'
                        self.task.put('end')
                        self.result.put({'new_urls':'end', 'data':'end'})
                        return
                    g = gevent.spawn(self.work_gevent, url)
                    g1 = gevent.spawn(self.gevent_print, 1)
                    g2 = gevent.spawn(self.gevent_print, 2)
                    g.join()
                    time.sleep(0.1)
            except EOFError, e:
                print "连接工作节点失败"
                return
            except Exception, e:
                print e
                print 'Crawl fali'

if __name__ == "__main__":
    spider = SpiderWork()
    spider.crawl()
