import scrapy
from fruit_legume.items import FruitLegumeItem


class FruitsLegumeSpider(scrapy.Spider):
    name = 'fruits_legume'

    def start_requests(self):
        yield scrapy.Request(url='https://www.greenpeace.fr/guetteur/calendrier/', callback=self.parse)

    def parse(self, response):
        box = response.xpath('//li[@class="month open"]')
        for elements in box:
            item = FruitLegumeItem()
            item["Month"] = f'{box.index(elements) + 1} : ' + elements.xpath('.//header/div/h2/text()').get()
            item["Fruits"] = [i.strip() for i in elements.xpath('.//section/article[2]/ul/li/text()').getall()]
            item["Legumes"] = [i.strip() for i in elements.xpath('.//section/article[1]/ul/li/text()').getall()]
            item["Cereales"] = [i.strip() for i in elements.xpath('.//section/article[3]/ul/li/text()').getall()]
            yield item
