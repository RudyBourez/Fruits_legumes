import scrapy


class FruitsLegumeSpider(scrapy.Spider):
    name = 'fruits_legume'

    def start_requests(self):
        urls = [
            'https://www.greenpeace.fr/guetteur/calendrier/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = {}
        box = response.xpath('//li[@class="month open"]').getall()
        for item in box:
            items["month"] = response.xpath('//h2/text()').get()
        return items,box
