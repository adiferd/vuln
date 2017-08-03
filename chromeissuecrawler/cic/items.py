# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id_cic = scrapy.Field()
    title = scrapy.Field()
    report_date = scrapy.Field()
    status = scrapy.Field()
    closed = scrapy.Field()
    description = scrapy.Field()
    pass
