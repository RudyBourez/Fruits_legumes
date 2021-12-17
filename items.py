# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class FruitLegumeItem(Item):
    Cereales = Field()
    Legumes = Field()
    Fruits = Field()
    Month = Field()

class PriceItem(Item):
    name = Field()
    type = Field()
    price = Field()



