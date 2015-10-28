# -*- coding: utf-8 -*-

import config
import discuz
import urllib2
import time
import re
import random

#content = r'[url=http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1565138]来参加河畔8周年环校跑吧[/url]'
content  = ("看看呢 路过帮顶一下","帮顶","看看呢","帮顶一下")
Life_Time = 20


class Sofa_machine(object):
    def __init__(self):
        self.my_account  = discuz.Discuz()
        self.aim_tid = 0
        self.last_succeed_tid = 0
        #self.life_time = Life_Time
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
                #print 'ready to reply to tid:' + str(self.tid)
                return int(fetch_success_info.group(1).encode('utf-8'))
            else:
                print 'fetch failed'
                return None



if __name__ == '__main__':
    sofa_machine  = Sofa_machine()
    #sofa_machine.aim_tid = sofa_machine.fetch_latest_tid()
    while True:
        sofa_machine.aim_tid = sofa_machine.fetch_latest_tid()
        if sofa_machine.last_succeed_tid == sofa_machine.aim_tid:
            time.sleep(10)
            print 'sleep'
        elif sofa_machine.my_account.reply(str(sofa_machine.aim_tid),content[random.randint(0,3)]):
            print 'post %d reply succeed ' % sofa_machine.aim_tid
            sofa_machine.last_succeed_tid = sofa_machine.aim_tid
            #sofa_machine.aim_tid = sofa_machine.aim_tid + 1
            #sofa_machine.life_time = Life_Time
        else:
            print 'reply failed :('
           # time.sleep(10)
           # if sofa_machine.life_time > 0:
           #     sofa_machine.life_time = sofa_machine.life_time - 1
           # if sofa_machine.life_time == 0:
           #     if sofa_machine.last_succeed_tid == sofa_machine.fetch_latest_tid():
           #         print 'no new tid'
           #         pass
           #     else:
           #         print 'restart reply'
           #         sofa_machine.aim_tid = sofa_machine.fetch_latest_tid()
           #         sofa_machine.life_time = Life_Time






