# -*- coding: utf-8 -*-

import config
import discuz
import re
import random
import time
import urllib2



content  = ("看看","试试","灌水","回帖加一","我能","再看看","路过一个的说","就是这样","西风来几日","一叶已先飞","新霁乘轻屐","初凉换熟衣","浅渠销慢水","疏竹漏斜晖","薄暮青苔巷","家僮引鹤归")
content2 = ("黑哥哥好厉害惹","抢不到啊","狙击狙击","快没水了","试试","水汽","再来","不要停")
if __name__ == '__main__':
    my_account  = discuz.Discuz()
    while True:
        username = raw_input('Please input username:')
        password = raw_input('Please input password:')
        if not my_account.login(username, password):
            print 'login failed'
        else:
            print 'login succeed'

            while True:
                try:
                    home_response  = my_account._get_response(url=config.WWURL).read()
                    lastpage_pattern = re.compile(r'class="last">.*?(\d+)</a>',re.S)
                    lastpage_search_result = lastpage_pattern.search(home_response)
                    if lastpage_search_result:
                        #print 'fetch lastpage_num succeed'
                        last_page = lastpage_search_result.group(1)
                        target_url= config.WWURL + '&extra=&page=' + last_page
                        target_url_response = my_account._get_response(url=target_url).read()

                        #print target_url
                        lastreply_pattern = re.compile(r'div id="post_\d+".*?postnum.*?em>.*?(\d+)',re.S)

                        lastreply_result = lastreply_pattern.findall(target_url_response)
                        #print lastreply_result
                        if lastreply_result:
                            if (len(lastreply_result) == 7):
                                print "reply 8"
                                my_account.reply(config.WWURL,content2[random.randint(0,7)])
                                time.sleep(6)
                            elif len(lastreply_result) == 17 and (not re.match(r'\d{3}77',lastreply_result[-1])) :
                                print "reply 18"
                                my_account.reply(config.WWURL,content2[random.randint(0,7)])
                                time.sleep(6)
                            elif re.match(r'\d{3}79',lastreply_result[-1]):
                                print "reply 80"
                                my_account.reply(config.WWURL,content2[random.randint(0,7)])
                                time.sleep(6)
                            else:
                                print len(lastreply_result)
                                #time.sleep(6)
                except urllib2.HTTPError, e:
                    print 'except:', e


