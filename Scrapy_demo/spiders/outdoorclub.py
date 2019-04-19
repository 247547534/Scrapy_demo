# -*- coding: utf-8 -*-
import scrapy


class OutdoorclubSpider(scrapy.Spider):
    name = 'outdoorclub'
    allowed_domains = ['outdoorclub.com']
    start_urls = ['https://m.outdoorclub.com.cn/?tdsourcetag=s_pcqq_aiomsg']

    def parse(self, response):
        with open("datas/outdoorclub.html","wb") as f:
            f.write(response.body)

