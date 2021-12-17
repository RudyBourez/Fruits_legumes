import scrapy
from fruit_legume.items import FruitLegumeItem


class FruitsLegumeSpider(scrapy.Spider):
    name = 'fruits_legume'

    def start_requests(self):
        yield scrapy.Request(url='https://www.greenpeace.fr/guetteur/calendrier/', callback=self.parse)

    def parse(self, response):
        item = FruitLegumeItem()
        box = response.xpath('//li[@class="month open"]')
        for elements in box:
            fruits = [i.strip() for i in elements.xpath('.//section/article[2]/ul/li/text()').getall()]
            for fruit in fruits:
                item["Month"] = elements.xpath('.//header/div/h2/text()').get()
                item["Type"] = "Fruits"
                item["Name"] = fruit
                yield item
            legumes = [i.strip() for i in elements.xpath('.//section/article[1]/ul/li/text()').getall()]
            for legume in legumes:
                item["Type"] = "Légumes"
                item["Name"] = legume
                yield item
            cereales = [i.strip() for i in elements.xpath('.//section/article[3]/ul/li/text()').getall()]
            for cereale in cereales:
                item["Type"] = "Céréales"
                item["Name"] = cereale
                yield item
            yield item
