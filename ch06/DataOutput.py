# coding:utf-8
import codecs

class DataOutput(object):
    def __init__(self):
        self.datas = []
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('download/baike.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write('<td width=100>%s</td>'%data["url"])
            fout.write('<td width=50>%s</td>' % data["title"])
            fout.write('<td width=1000>%s</td>' % data["summary"])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
        fout.close()