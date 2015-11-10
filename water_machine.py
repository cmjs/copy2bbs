# -*- coding: utf-8 -*-

import config
import discuz
import re
import random
import time
import urllib2



content  = ("看看","试试","灌水","回帖加一","我能","再看看","路过一个的说","就是这样")

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
                    home_response  = my_account._get_response(url=config.WATERURL).read()
                    lastpage_pattern = re.compile(r'class="last">.*?(\d+)</a>',re.S)
                    lastpage_search_result = lastpage_pattern.search(home_response)
                    if lastpage_search_result:
                        #print 'fetch lastpage_num succeed'
                        last_page = lastpage_search_result.group(1)
                        target_url= config.WATERURL + '&extra=&page=' + last_page
                        target_url_response = my_account._get_response(url=target_url).read()

                        #print target_url
                        lastreply_pattern = re.compile(r'div id="post_(\d+)".*?uid=(\d+)',re.S)

                        lastreply_result = lastreply_pattern.findall(target_url_response)
                        if lastreply_result:
                            if config.USERUID != lastreply_result[-1][-1]:
                                print "can reply"
                                my_account.reply(config.WATERURL,content[random.randint(0,7)])
                                time.sleep(10)
                                print "2 lian"
                                my_account.reply(config.WATERURL,content[random.randint(0,7)])
                            else:
                                print "will 3 lian"
                                time.sleep(10)
                except urllib2.HTTPError, e:
                    print 'except:', e


