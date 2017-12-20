# -*- coding: utf-8 -*-
import scrapy

class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in xrange(1,2):
        url = 'https://www.qiushibaike.com/hot/page/'+str(i)+'/'
        start_urls.append(url)

    def parse(self, response):
        subSelector = response.xpath('//div[@class="article block untagged mb15" and @id]')
        items = []
        for sub in subSelector:
            for sub in subSelector:
                item = QiushiItem()
                item['author'] = sub.xpath('.//h2/text()').extract()[0]
                item['content'] = sub.xpath('.//div[@class="content"]/text()').extract()[0]
                item['img'] = sub.xpath('.//img/@src').extract()
                item['funNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[0]
                try:
                    item['talkNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[1]
                except IndexError:
                    item['talkNum'] = '0'
                items.append(item)
            return items

