# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id_commit = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    commiter = scrapy.Field()
    commit_message = scrapy.Field()
    time = scrapy.Field()
    difTree = scrapy.Field()
    pass
