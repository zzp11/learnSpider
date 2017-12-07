#-coding:utf-8
from bs4 import BeautifulSoup

from pprint import pprint
from functools import partial
pprint =partial(pprint, indent = 0)

soup = BeautifulSoup(open('server.html'), 'lxml')
print soup.a.parent

import  random
import time

while 1:
    print random.randint(0, 1000)
    time.sleep(0.5)
