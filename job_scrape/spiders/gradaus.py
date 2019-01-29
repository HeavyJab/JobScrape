# -*- coding: utf-8 -*-
import scrapy

class GradausSpider(scrapy.Spider):
    name = 'gradaus'
    start_urls = ['https://gradaustralia.com.au/search-jobs/region/victoria/']

    def parse(self, response):
        for url in response.xpath('//div[@class="content-footer"]/div[@class="field field-name-node-link field-type-ds field-label-hidden"]//@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)

        ads = {}
        ads['job_title'] = response.xpath('//div[@class="views-field views-field-title"]/h1[@class="field-content"]//text()').extract_first()
        ads['recruiter'] = response.xpath('//div[@class="content-secondary"]//div[@class="field-item even"]/span//text()').extract_first()
        ads['job_type'] = response.xpath('//div[@class="views-field views-field-taxonomy-vocabulary-46"]/div[@class="field-content"]//text()').extract_first()
        ads['vacancy'] = response.xpath('//div[@class="views-field views-field-field-ad-vac-vacancies"]/div[@class="field-content"]//text()').extract_first()
        ads['salary'] = response.xpath('//div[@class="views-field views-field-field-ad-vac-salary"]/div[@class="field-content"]//text()').extract_first()
        ads['location'] = response.xpath('//div[@class="views-field views-field-field-ad-vac-locations"]/div[@class="field-content"]//text()').extract_first()
        ads['start_date'] = response.xpath('//div[@class="views-field views-field-field-ad-vac-start-date"]/div[@class="field-content"]//text()').extract_first()
        ads['level_of_study'] = response.xpath('//div[@class="views-field views-field-field-minimum-level-study"]/div[@class="field-content"]//text()').extract_first()
        ads['academic_results'] = response.xpath('//div[@class="views-field views-field-taxonomy-vocabulary-51"]/div[@class="field-content"]//text()').extract_first() 
        ads['open_date'] = response.xpath('//div[@class="views-field views-field-field-field-job-apps-open"]/div[@class="field-content"]//text()').extract_first()
        ads['close_date'] = response.xpath('//div[@class="views-field views-field-field-ad-vac-closing-date"]/div[@class="field-content"]//text()').extract_first()
        ads['job_desc'] = response.xpath('//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"]//div[@class="field-item even"]/*[not(self::script)]//text()').extract()
        ads['application_url'] = response.xpath('//div[@class="field field-name-ad-vac-url field-type-ds field-label-hidden"]//div[@class="field-item even"]//@href').extract_first()
        yield ads





