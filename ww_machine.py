# -*- coding: utf-8 -*-

import config
import discuz
import re
import random
import time
import urllib2



content  = ("看看","试试","灌水","回帖加一","我能","再看看","路过一个的说","就是这样","西风来几日","一叶已先飞","新霁乘轻屐","初凉换熟衣","浅渠销慢水","疏竹漏斜晖","薄暮青苔巷","家僮引鹤归")
content2 = ("黑哥哥好厉害惹","抢不到啊","狙击狙击","快没水了","试试","水汽","再来","不要停")
content3 = ("555555","666666")
content4 = "80L"

last_page_url = "http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1570810&extra=&page=9999＆mobile=1"

if __name__ == '__main__':
    my_account  = discuz.Discuz()
    while True:
        username = raw_input('Please input username:')
        password = raw_input('Please input password:')
        mode     = raw_input('choose mode: 1->*8  2->80 08:')
        if not my_account.login(username, password):
            print 'login failed'
        else:
            print 'login succeed'
            #lastreply_pattern = re.compile(r'div id="post_\d+".*?postnum.*?em>.*?(\d+)',re.S)
            lastreply_pattern = re.compile(r'postnum.*?em>.*?(\d+)',re.S)
            pattern_79  = re.compile(r'\d{3}79')
            pattern_77  = re.compile(r'\d{3}77')
            pattern_07  = re.compile(r'\d{3}07')
            while True:
                try:
                    target_url_response = my_account._get_response(url=last_page_url).read()



                    #print target_url_response
                    lastreply_result = lastreply_pattern.findall(target_url_response)
                    #print lastreply_result


                    if lastreply_result:
                        if mode == '1':
                            if (len(lastreply_result) == 7):
                                print "reply 8"
                                my_account.reply(config.WWURL,content3[random.randint(0,1)])
                                time.sleep(5)
                            elif (len(lastreply_result) == 19):
                                #if re.match(r'\d{3}79',lastreply_result[-1]):
                                if pattern_79.match(lastreply_result[-1]):
                                    my_account.reply(config.WWURL,content3[random.randint(0,1)])
                                    print "reply 80"
                                else:
                                    print "ignore"
                                    time.sleep(5)
                            elif len(lastreply_result) == 17:
                                if (not pattern_77.match(lastreply_result[-1])) :
                                    print "reply 18"
                                    my_account.reply(config.WWURL,content3[random.randint(0,1)])
                                    time.sleep(5)
                                else:
                                    print "77 ignore"
                            else:
                                print len(lastreply_result)
                        elif mode == '2':
                            if (len(lastreply_result) == 19):
                                #if re.match(r'\d{3}79',lastreply_result[-1]):
                                if pattern_79.match(lastreply_result[-1]):
                                    my_account.reply(config.WWURL,content3[random.randint(0,1)])
                                    print "reply 80"
                                else:
                                    print "ignore"
                            elif (len(lastreply_result) == 7):
                                #if re.match(r'\d{3}07',lastreply_result[-1]):
                                if pattern_07.match(lastreply_result[-1]):
                                    my_account.reply(config.WWURL,content3[random.randint(0,1)])
                                    print "reply 08"
                                else:
                                    print "ignore"
                            else:
                                print len(lastreply_result)
                            #time.sleep(6)
                except urllib2.HTTPError, e:
                    print 'except:', e


