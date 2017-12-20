# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem

class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in xrange(1,2):
        url = 'https://www.qiushibaike.com/hot/page/'+str(i)+'/'
        start_urls.append(url)
    def parse(self, response):
        subSelector = response.xpath('//div[@class="article block untagged mb15 typs_hot" and contains(@id,"qiushi_tag_")]')
        items = []
        for sub in subSelector:
            for sub in subSelector:
                item = QiushiItem()
                str = sub.xpath('.//h2/text()').extract()
                if str:
                    item['author'] = sub.xpath('.//h2/text()').extract()[0]
                else:
                    item['author'] = '无名'
                ct = sub.xpath('.//div[@class="content"]/span/text()').extract()
                if ct:
                    item['content'] = sub.xpath('.//div[@class="content"]/span/text()').extract()[0]
                else:
                    item['content'] = ''
                item['img'] = sub.xpath('.//img/@src').extract()
                fn = sub.xpath('.//i[@class="number"]/text()')
                if fn:
                    item['funNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[0]
                    try:
                        item['talkNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[1]
                    except IndexError:
                        item['talkNum'] = '0'
                else:
                    item['funNum'] = '0'
                    item['talkNum'] = 0
                items.append(item)
            return items

