# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobScrapeItem(scrapy.Item):
    job_title = scrapy.Field()
    recruiter = scrapy.Field()
    job_type = scrapy.Field()
    vacancy = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    level_of_study = scrapy.Field()
    academic_results = scrapy.Field()
    open_date = scrapy.Field()
    close_date = scrapy.Field()
    job_desc = scrapy.Field()
    application_url = scrapy.Field()
    
