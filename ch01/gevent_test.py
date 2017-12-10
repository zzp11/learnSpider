from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import time

def run_task(url):
    print "visit --> {}".format(url)
    try:
        resp = urllib2.urlopen(url)
        data = resp.read()
        print "{} bytes received from {}".format(len(data), url)
        return data
    except Exception, e:
        print e

def test_yield(urls):
    for url in urls:
        yield run_task(url)

def run_yield(urls):
    for data in test_yield(urls):
        print "get data"

if __name__ == "__main__":
    while True:
        url = "https://github.com/"
        gevent.spawn(run_task, url)
        time.sleep(1)

    urls = ["https://github.com/", "https://www.python.org/", "http://www.cnblogs.com/"]
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)
    #for url in urls:
     #   gevent.spawn(run_task, url)
    for i in range(3):
        time.sleep(1)
        print "sleep {} s".format(i+1)