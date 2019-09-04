# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ARQUIVO DESTINADO A TRABALHAR COM BANCO DE DADOS


class NoticiasPipeline(object):
    def open_spider(self, spider):
        return spider

    def close_spider(self, spider):
        return spider

    def process_item(self, item, spider):
        return item
