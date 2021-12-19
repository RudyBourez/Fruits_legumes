# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class FruitLegumeItem(Item):
    Type = Field()
    Name = Field()
    Month = Field()

class PriceItem(Item):
    Name = Field()
    Type = Field()
    Price = Field()

class RecettesItem(Item):
    Name = Field()
    Ingredients = Field()
    Link = Field()
    Note = Field()
    Time = Field()