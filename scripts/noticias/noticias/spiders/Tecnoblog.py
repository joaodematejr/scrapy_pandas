# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
import json
from noticias.items import NoticiasItem

""" CONFIGURACAOES MONGODB """
configMongoDb = MongoClient('localhost', 27017)
banco = configMongoDb['mongo_tecnoblog']


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
        for article in response.css("article"):
            link = article.css("div.texts h2 a::attr(href)").extract_first()
            yield response.follow(link, self.parse_article)
        next_page = response.css('a#mais::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        link = response.url
        title = response.css("title ::text").extract_first()
        author = response.css("span.author ::text").extract_first()
        text = "".join(response.css("div.entry ::text").extract())
        notice = NoticiasItem(title=title, author=author, text=text, link=link)
        """ DADOS A SER TRATATOS A PARTIR DAQUI  """
        converterDadosJson = {'link': link, 'texto': text,
                              'autor': author, 'noticia': notice}
        print('=============== INICIO ===============')
        print('dadosJson ', converterDadosJson)
        print('=============== FIM ===============')
        """ FINALIZAÇÃO DO TRATAMENTO DE DADOS AQUI  """

        """ TESTANDO CONEXAO COM BANCO DE DADO  """
        db = configMongoDb.pymongo_test
        dados = db.dados
        """ SALVAR DADOS NO MONGODB """
        dadosInserirBanco = dados.insert_many([converterDadosJson])

        yield notice
