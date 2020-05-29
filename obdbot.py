# -*- coding: utf-8 -*-
import scrapy


class ObdbotSpider(scrapy.Spider):
    name = 'obdbot'
    allowed_domains = ['www.obd-codes.com/trouble_codes/toyota/']
    start_urls = ['http://www.obd-codes.com/trouble_codes/toyota//']

    def parse(self, response):
        pass
