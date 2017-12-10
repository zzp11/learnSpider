#coding: utf-8
import cPickle
import hashlib

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#self.load_progress('new_urls.txt')
        self.old_urls = set()#self.load_progress('old_urls.txt')

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        print "new_url_size:", len(self.new_urls)
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)

    def save_progress(self, path, data):
        with open(path, 'wb') as f:
            cPickle.dump(data, f)

    def load_progress(self, path):
        print '[+] 从文件加载进度： %s' % path
        try:
            with open(path, 'rb',) as f:
                tmp = cPickle.load(f)
                return tmp
        except:
            print '[!] 无进度文件， 创建：%s' % path
        return set()
