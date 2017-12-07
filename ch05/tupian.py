#coding:utf-8
import urllib
from lxml import etree
import requests
import os

def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    per = min(per, 100)
    print '已完成：{}'.format(per)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    path = "img/" + str(i) + '.jpg'
    urllib.urlretrieve(img_url, path, Schedule)
    i += 1
