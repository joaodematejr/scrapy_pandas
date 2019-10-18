# -*- coding: utf-8 -*-
import scrapy


class StartupSpider(scrapy.Spider):
    name = 'Startup'
    allowed_domains = ['startupbase.com.br']
    start_urls = ['http://startupbase.com.br/']

    def parse(self, response):
        pass
