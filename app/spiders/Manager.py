# -*- coding: utf-8 -*-
import scrapy


class ManagerSpider(scrapy.Spider):
    name = 'Manager'
    url_base = 'https://www.manager.com.br/empregos-desenvolvedor-javascript/'
    start_urls = [url_base]

    def parse(self, response):

        print("Em Processamento: " + response.url)
        """ PROPRIEDADES CSS  """
        div_lista_vagas = '//div[@id="lista-resultado-busca-vagas"]/article[@class="vaga hlisting"]/header/h2'
        div_proxima_pagina = '//div[contains(@class, "pagination pagination-centered hidden-print")]//a[@rel="next nofollow"]/@href'
        css_classe_a = './a/@href'

        itens_vagas = response.xpath(div_lista_vagas)
        for vaga in itens_vagas:
            url_vagas = vaga.xpath(css_classe_a).extract_first()
            yield scrapy.Request(url=url_vagas, callback=self.detalhes_vagas)
        proxima_pagina = response.xpath(div_proxima_pagina)
        if proxima_pagina:
            yield scrapy.Request(url=proxima_pagina.extract_first(), callback=self.parse)

    def detalhes_vagas(self, response):
        """ PROPRIEDADES CSS  """
        css_titulo = '//header[@class="page-header"]/meta'
        css_cidade = '//dl[@class="location adr"]/dd[@class="clear-none"]/span'
        css_salario = '//div[@class="sub-item"]/dl/dd/meta'
        css_descricao = '//div[@class="description"]/p'

        titulo = response.xpath(css_titulo).extract_first()
        cidade = response.xpath(css_cidade).extract_first()
        salario = response.xpath(css_salario).extract_first()
        descricao = response.xpath(css_descricao).extract_first()
        yield{'Titulo': titulo, 'Cidade': cidade, 'Salario': salario, 'Descricao': descricao, }
