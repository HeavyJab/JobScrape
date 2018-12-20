# -*- coding: utf-8 -*-
import scrapy


class DatascienceSpider(scrapy.Spider):
    name = 'datascience'
    start_urls = ['https://www.seek.com.au/data-scientist-jobs']

    def parse(self, response):
        ads = response.xpath('//div[@data-sol-meta]').extract()
        yield {'ads': ads}
