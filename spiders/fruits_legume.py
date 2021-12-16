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
        box = response.xpath('//li[@class="month open"]')
        for item in box:
            yield{
                "month" : item.xpath('.//header/div/h2/text()').get(),
                "vegetables" : item.xpath('.//section/article/ul/li/text()').getall(),
            }
