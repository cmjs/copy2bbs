# -*- coding: utf-8 -*-

import config
import discuz
import urllib2
import time
import re

content = r'[url=http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1565138]来参加河畔8周年环校跑吧[/url]'

class Sofa_machine(object):
    def __init__(self):
        self.my_account  = discuz.Discuz()
        if not self.my_account.login(config.USERNAME, config.PASSWORD):
            self.login_flag = False
            print 'login failed'
        else:
            self.login_flag = True
            print 'login succeed'


    def fetch_latest_tid(self):
        if self.login_flag == True:
            request =  urllib2.Request(config.DOMAIN)
            response = urllib2.urlopen(request).read().decode('utf-8')
            #print response
            latest_pattern = re.compile(ur"最新发表</span>.*?viewthread&tid=(\d{7})",re.S)
            fetch_success_info = latest_pattern.search(response)
            if fetch_success_info:
                print 'fetch succeed'
                self.tid =  int(fetch_success_info.group(1).encode('utf-8'))
                #print 'ready to reply to tid:' + str(self.tid)
                return self.tid
            else:
                print 'fetch failed'
                return None



if __name__ == '__main__':
    sofa_machine  = Sofa_machine()
    latest_tid = sofa_machine.fetch_latest_tid()
    sofa_machine.tid = sofa_machine.tid
    while True:
        if sofa_machine.my_account.reply(str(sofa_machine.tid),content):
            print 'post %d reply succeed' % sofa_machine.tid
            sofa_machine.tid = sofa_machine.tid + 1
        else:
            print 'sleep'
            time.sleep(10)





