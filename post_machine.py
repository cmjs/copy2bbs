# -*- coding: utf-8 -*-

import config
import discuz
import spider


if __name__ == '__main__':
    my_account  = discuz.Discuz()
    if not my_account.login(config.USERNAME, config.PASSWORD):
        print 'login failed'
    else:
        print 'login succeed'
        my_spider = spider.Spider('your_url')
        if my_spider.spide():
            print 'spide succeed'
            if my_account.post_new('312',my_spider.subject,my_spider.content):
                print 'post succeed'
            else:
                print 'post failed'
        else:
            print 'spide failed'


