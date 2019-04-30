# -*- coding: utf-8 -*-
import scrapy
from Scrapy_demo.items import DemoItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['demo.com']
    start_urls = ['http://www.lis99.com/activity/xQygOhuZ_d.html']
    custom_settings = {
        'ITEM_PIPELINES':{'Scrapy_demo.pipelines.DemoPipeline':600}
    }

    def parse(self, response):
        item = DemoItem()
        item['title'] = response.xpath('/html/body/div[3]/div[2]/div[1]/p/text()').extract()
        item['start_addr'] = response.xpath('/html/body/div[3]/div[2]/div[2]/span[1]/text()').extract()
        item['days'] = response.xpath('/html/body/div[3]/div[2]/div[2]/span[4]/text()').extract()
        item['attr'] = response.xpath('/html/body/div[3]/div[2]/div[2]/span[2]/text()').extract()
        item['price'] = response.xpath('/html/body/div[3]/div[2]/div[3]/div/span[3]/span/span/text()').extract()
        return item