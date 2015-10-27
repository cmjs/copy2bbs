# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
import re

import config

class Discuz(object):
    def __init__(self):
        self.response_page = ''  # response的对象（不含read）
        self.formhash = ''  # 没有formhash不能发帖

        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

        self.formhash_pattern = re.compile(r'<input type="hidden" name="formhash" value="([0-9a-zA-Z]+)" />')

        self.post_success_pattern = re.compile(r'<meta name="keywords" content="(?u)(.+)" />')  # 发帖成功时匹配
        self.post_fail_pattern = re.compile(r'<div id="messagetext" class="alert_error">')  # 发贴失败时匹配
        self.post_error_pattern = re.compile(r'<p>(?u)(.+)</p>')  # 发贴失败的错误信息

    def login(self, username, password, questionid = 0, answer = ''):
        postdata = {
                         'loginfield': config.LOGINFIELD,
                         'username': username,
                         'password': password,
                         'questionid': questionid,
                         'answer': answer,
        }

        login_success_pattern = re.compile(ur"\('succeedlocation'\).innerHTML = '(?u)(.+)，现在将转入登录前页面';")
        login_fail_pattern = re.compile(r"{errorhandle_\('(?u)(.+)',")

        # 取得登录成功/失败的提示信息
        self.response_page = self._get_response(config.LOGINURL, postdata)
        login_tip_page = self.response_page.read().decode('utf-8')
        #print '======================='
        #print login_tip_page
        #print '======================='
        login_success_info = login_success_pattern.search(login_tip_page)
        login_fail_info = login_fail_pattern.search(login_tip_page)

        # 显示登录成功/失败信息
        if login_success_info:
            print login_success_info.group(1)
        #    print '------------------------'
        #    print self._get_response(config.HOMEURL).read()
        #    print '------------------------'
            self.formhash = self._get_formhash(self._get_response(config.HOMEURL).read())
            return True
        elif login_fail_info:
            print login_fail_info.group(1)
        else:
            print '无法获取登录状态'

        return False

    def _get_response(self, url, data = None):
        if data is not None:
            req = urllib2.Request(url, urllib.urlencode(data))
        else:
            req = urllib2.Request(url)

        response = self.opener.open(req)
        return response

    def _get_formhash(self, page_content):
        self.formhash = self.formhash_pattern.search(page_content.decode('utf-8')).group(1)
        print 'formhash =>' + self.formhash
        return self.formhash

    def post_new(self, fid, subject, message):
        postdata = {
                    'subject': subject,
                    'message': message,
                    'typeid':1096,
                    'formhash': self.formhash,
        }

        base_url = config.POSTURL
        url = base_url.replace('FID', fid)

        self.response_page = self._get_response(url, postdata)
        print postdata['subject']
        prefix = '主题 "%s" ' %postdata['subject']
        return self.__verify_post_status(prefix)
    def reply(self, tid, message):
        postdata = {
                    'message': message,
                    'formhash': self.formhash,
        }

        base_url = config.REPLYURL
        url = base_url.replace('TID', tid)
        self.response_page = self._get_response(url, postdata)

        prefix = '回复 "%s" ' % self._interception(message, 80)
        return  self.__verify_post_status(prefix)

    def __verify_post_status(self, prefix):
        page_content_utf8 = self.response_page.read().decode('utf-8')

        if self.post_success_pattern.search(page_content_utf8):
            print "%s发布成功！" % prefix
            return True
        elif self.post_fail_pattern.search(page_content_utf8):
            post_error_message = self.post_error_pattern.search(page_content_utf8)
            try:
                print "%s发布失败！原因是：%s。" % (prefix, post_error_message.group(1))
            except:
                print "%s发布失败！原因是：未知原因。" % prefix
            return False
        else:
            print "无法确定%s发布状态" % prefix
            return False