import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fruit_legume.items import RecettesItem

class RecettesSpider(CrawlSpider):
    name = 'recettes'
    allowed_domains = ['marmiton.org']
    start_urls = ['https://www.marmiton.org/recettes/top-internautes.aspx',
    ]
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="topResearchCard"]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="MRTN__sc-1gofnyi-2 gACiYG"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="SHRD__sc-1ymbfjb-1 MTkAM"]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="recipe-card-link"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="content"]/div[3]/div[1]/div/div[1]/div/ul/li/a'), follow=True)
    )

    def parse_item(self, response):
        item = RecettesItem()
        item['Name'] = response.xpath('//h1/text()').get()
        item['Ingredients'] = [item.capitalize() for item in response.xpath('//span[@class="RCP__sc-8cqrvd-3 itCXhd"]/text()').getall()]
        try:
            item['Ingredients'].extend([item.capitalize() for item in response.xpath('//span[@class="RCP__sc-8cqrvd-3 cDbUWZ"]/text()').getall()])
        except:
            item['Ingredients'] = [item.capitalize() for item in response.xpath('//span[@class="RCP__sc-8cqrvd-3 cDbUWZ"]/text()').getall()]
        item["Link"] = response.request.url
        item["Note"] = "".join(response.xpath('//span[@class="SHRD__sc-10plygc-0 jHwZwD"]/text()').getall())
        item["Time"] = response.xpath('//div[1]/span/p[@class="RCP__sc-1qnswg8-1 iDYkZP"]/text()').get()
        yield item