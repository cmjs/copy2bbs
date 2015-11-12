# -*- coding: utf-8 -*-

import config
import discuz
import spider


if __name__ == '__main__':
    my_account  = discuz.Discuz()
    username = raw_input('Please input username:')
    password = raw_input('Please input password:')
    if not my_account.login(username, password):
        print 'login failed'
    else:
        print 'login succeed'
        my_spider = spider.Spider('http://iranshao.com/articles/2110-yuki-kawauchi')
        if my_spider.spide():
            print 'spide succeed'
            if my_account.post_new('312',my_spider.subject,my_spider.content):
                print 'post succeed'
            else:
                print 'post failed'
        else:
            print 'spide failed'


