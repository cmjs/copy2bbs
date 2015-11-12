# -*- coding: utf-8 -*-

import config
import discuz
import re
import random
import time
import urllib2



content  = ("看看","试试","灌水","回帖加一","我能","再看看","路过一个的说","就是这样","西风来几日","一叶已先飞","新霁乘轻屐","初凉换熟衣","浅渠销慢水","疏竹漏斜晖","薄暮青苔巷","家僮引鹤归")


last_page_url = "http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1559009&extra=&page=9999"

if __name__ == '__main__':
    my_account  = discuz.Discuz()
    while True:
        username = raw_input('Please input username:')
        password = raw_input('Please input password:')
        if not my_account.login(username, password):
            print 'login failed'
        else:
            print 'login succeed'
            lastreply_pattern = re.compile(r'div id="post_(\d+)".*?uid=(\d+)',re.S)
            while True:
                try:
                    target_url_response = my_account._get_response(url=last_page_url).read()
                    lastreply_result = lastreply_pattern.findall(target_url_response)
                    if lastreply_result:
                        if config.USERUID != lastreply_result[-1][-1]:
                            print "can reply"
                            my_account.reply(config.WATERURL,content[random.randint(0,15)])
                            time.sleep(10)
                            print "2 lian"
                            my_account.reply(config.WATERURL,content[random.randint(0,15)])
                        else:
                            print "will 3 lian"
                            time.sleep(10)
                except urllib2.HTTPError, e:
                    print 'except:', e


