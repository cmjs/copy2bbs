# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2


class Spider(object):
    def __init__(self,url):
        self.spiderUrl = url
        self.subject=''
        self.content=''
    def spide(self):
        self.subject=''
        self.content=''
        try:
            request = urllib2.Request(self.spiderUrl)
            response = urllib2.urlopen(request)
            soup = BeautifulSoup(response.read().decode('utf-8'))

            self.subject = soup.title.string.output_ready()
            self.subject = self.subject.encode('utf-8')

            self.content = '[b]' + soup.find("div",class_="article-experpt explain").string.output_ready() + '[/b]' + '\n'

            main_body = soup.find("div",class_ ="js-article-body")
            for child in main_body.children:
                if child.string:
                    self.content = self.content + '\t' + child.string.output_ready() +'\n'
                elif child.contents:
                #    if child.contents[0].name=='strong':
                #        self.content = self.content + '[color=Sienna]'  + child.string.output_ready() +'[/color]' +'\n'
                    if child.contents[0].name=='img':
                        self.content = self.content + '[align=center][img=660,440]' + child.contents[0]['src'] + '[/img][/align]'+'\n'


            self.content = self.content.encode('utf-8')
            self.content = '[font=微软雅黑]' + self.content +'[/font]'+ '\n\n\n\n ' +'本文转自' + self.spiderUrl + '\n' + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t-----自动转贴'
            print (self.content)
            return True
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
            return False


if __name__ == '__main__':
    spider  = Spider('you url')
    spider.spide()

