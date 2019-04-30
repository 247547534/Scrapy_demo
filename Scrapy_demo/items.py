# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    send_addr = scrapy.Field()
    send_nums = scrapy.Field()
    #说明
    explain = scrapy.Field()
    #授权书
    authorization = scrapy.Field()


class CrawlDemoItem(scrapy.Item):
    title = scrapy.Field()


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    start_addr = scrapy.Field()
    attr = scrapy.Field()
    days = scrapy.Field()
    price = scrapy.Field()
