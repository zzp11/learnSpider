# coding:utf-8
import json
from bs4 import BeautifulSoup
import requests
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/', headers = headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string.encode('utf-8')
        print h2_title
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            math = re.search(r'.*?\[(.*)\]\s(.*)', box_title)
            date = math.group(1).encode('utf-8')
            real_title = math.group(2).encode('utf-8')
            list.append({'href':href, 'date':date, "title":real_title})
        content.append({'title':h2_title, 'content':list})
with open('qiye.json', 'wb') as fp:
    json.dump(content, fp = fp, indent=4, ensure_ascii=False)