#! /usr/bin/env python
#-*- coding: utf-8 -*-

__Author__ = 'rico201702@163.com'

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = "Mozilla/5.0 （Windows NT 6.1） AppleWebKit/536.3 （KHTML，likeGe cko） Chrome/19.0.1061.1 Safari/536.3"
        request.headers.setdefault('User-Agent',ua)

class CustomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://117.6.161.118:53281'
