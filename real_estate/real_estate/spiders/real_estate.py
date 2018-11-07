import scrapy

class RESpider(scrapy.Spider):
    name = "real_estate"

    def start_requests(self):
        urls = [
            'https://www.realestate.com.au/buy/property-house-unit+apartment-townhouse/map-1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'real_estate.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % 're')

