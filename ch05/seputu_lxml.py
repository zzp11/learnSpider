from lxml import etree
import requests
import re
import csv

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/', headers=headers)

rows = []
html = etree.HTML(r.text)
div_mulus = html.xpath('.//*[@class="mulu"]')
#print "div_mulus", len(div_mulus)
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    #print div_h2
    if len(div_h2) > 0:
        h2_title = div_h2[0].encode('utf-8')
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0].encode('utf-8')
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\[(.*)\]\s+(.*)')
            math = pattern.search(box_title)
            #print math
            if math != None:
                date = math.group(1).encode('utf-8')
                real_title = math.group(2).encode('utf-8')
                content = (h2_title, real_title, href, date)
                #print content
                rows.append(content)

headers = ['title', 'real_title', 'href', 'date']
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f, )
    f_csv.writerow(headers)
    f_csv.writerows(rows)

