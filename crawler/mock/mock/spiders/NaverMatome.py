# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from mock.items import NaverMatomeItem

class NaverMatomeSpider(BaseSpider):
    name = 'naver_matome'
    allowed_domains = ['matome.naver.jp']

    start_urls = []
    max_pages = 50
    for i in xrange(max_pages):
        start_urls.append('http://matome.naver.jp/?page={0}'.format(i))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul[@class="mdTopMTMList01List"]/li')
        items = []
        for site in sites:
            item = NaverMatomeItem()
            item['title'] = site.select('div/h3/a/@title').extract()[0]
            item['user'] = site.select('div/div/p[@class="mdTopMTMList01UserName"]/@title').extract()[0]
            item['view'] = site.select('div/div/p[@class="mdTopMTMList01PVCount"]/span[@class="mdTopMTMList01PVCountNum"]/text()').extract()[0]
            items.append(item)
        for item in items:
            yield item