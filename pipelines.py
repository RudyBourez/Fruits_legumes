# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging

class FruitLegumePipeline(object):

    collection_name = 'vegetables'

    def __init__(self, mongo_host, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # pull in information from settings.py
        return cls(
            mongo_host=crawler.settings.get('MONGO_HOST'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # initializing spider
        # opening db connection
        self.client = pymongo.MongoClient(self.mongo_host)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        # how to handle each post   
        self.db[self.collection_name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item

# class PricePipeline(object):

#     collection_name = 'price'

#     def __init__(self, mongo_host, mongo_db):
#         self.mongo_host = mongo_host
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         # pull in information from settings.py
#         return cls(
#             mongo_host=crawler.settings.get('MONGO_HOST'),
#             mongo_db=crawler.settings.get('MONGO_DB')
#         )

#     def open_spider(self, spider):
#         # initializing spider
#         # opening db connection
#         self.client = pymongo.MongoClient(self.mongo_host)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         # clean up when spider is closed
#         self.client.close()

#     def process_item(self, item, spider):
#         # how to handle each post   
#         self.db[self.collection_name].insert_one(dict(item))
#         logging.debug("Post added to MongoDB")
#         return item

    