from gevent import monkey; monkey.patch_all()
import urllib2
from gevent.pool import Pool

def run_task(url):
    print 'visit --> {}'.format(url)
    try:
        resp = urllib2.urlopen(url)
        data = resp.read()
        print '{} bytes received from {} '.format(len(data), url)
    except Exception, e:
        print e
    return 'url: {} --> finish'.format(url)

if __name__ == '__main__':
    pool = Pool(2)
    urls = ["https://github.com/", "https://www.python.org/", "http://www.cnblogs.com/"]
    res = pool.map(run_task, urls)
    print res