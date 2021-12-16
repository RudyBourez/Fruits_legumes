import scrapy
from fruit_legume.items import FruitLegumeItem

class FruitsLegumeSpider(scrapy.Spider):
    name = 'fruits_legume'

    def start_requests(self):
        urls = [
            'https://www.greenpeace.fr/guetteur/calendrier/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        box = response.xpath('//li[@class="month open"]')
        for elements in box:
            item = FruitLegumeItem()
            item["month"] = elements.xpath('.//header/div/h2/text()').get(),
            item["fruits"] = elements.xpath('.//section/article[2]/ul/li/text()').getall()
            item["legumes"] = elements.xpath('.//section/article[1]/ul/li/text()').getall()
            item["cereales"] = elements.xpath('.//section/article[3]/ul/li/text()').getall()
            yield item
