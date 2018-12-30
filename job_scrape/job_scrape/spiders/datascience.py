# -*- coding: utf-8 -*-
import scrapy


class DatascienceSpider(scrapy.Spider):
    name = 'datascience'
    start_urls = ['https://www.seek.com.au/data-scientist-jobs/in-All-Melbourne-VIC']

    def parse(self, response):
        for url in response.xpath('//div[@data-sol-meta]/article/span/div[@href]/@href').extract():
            url = response.urljoin(url)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

        ads = {}
        ads['job_date'] = response.xpath('//section[@aria-labelledby="jobInfoHeader"]//text()').extract()
        yield ads
