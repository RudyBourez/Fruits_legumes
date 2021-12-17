import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fruit_legume.items import PriceItem

class PriceSpider(CrawlSpider):
    name = 'price'
    allowed_domains = ['rnm.franceagrimer.fr']
    start_urls = ['https://rnm.franceagrimer.fr/prix?FRUITS-ET-LEGUMES',]
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="listunproduit"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = PriceItem()

        item['Name'] = response.xpath('//h1/text()').get()
        item['Type'] = response.xpath('//div[@class="signet"]/a[4]/text()').get()[2:]
        item["Price"] = response.xpath('//table[@class="tabcot"]/tbody/tr/td[@class="tdcotr"]/strong/text()').getall()
        for element in item["Price"]:
            if element == "\xa0":
                item["Price"].remove(element)
        yield item
