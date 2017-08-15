# -*- coding:utf-8 -*-
import scrapy
from chlog.items import ChlogItem

class CommitSpider(scrapy.Spider):
    name= "commit"
    allowed_domain = ["chromium.googlesource.com"]

    start_urls = ["https://chromium.googlesource.com/chromium/src/"]


    item = ChlogItem()
    title = ''
    def parse(self,response):
        self.title = response.xpath("/html/body/div/div/div[3]/div[2]/ol/li[1]/a[2]/text()").extract()
        for detail_href in response.css('.CommitLog li a::attr(href)').extract(): #detail link
            yield scrapy.Request(response.urljoin(detail_href),
                                callback=self.parse_commit_detail)
        next_page = response.css('.LogNav a::attr(href)').extract()[-1] # next page link is at the end of page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_commit_detail(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_css_and_re(query, re_expression):
            result = response.css(query).re(re_expression)
            if len(result) > 0:
                return result[0]

        self.item['id_commit'] = response.xpath("/html/body/div/div/div[2]/table/tr[1]/td[1]/text()").extract(),
        self.item['title'] = self.title
        self.item['author'] = response.xpath("/html/body/div/div/div[2]/table/tr[2]/td[1]/text()").extract(),
        self.item['time'] = response.xpath("/html/body/div/div/div[2]/table/tr[2]/td[2]/text()").extract(),
        self.item['commiter'] = response.xpath("/html/body/div/div/div[2]/table/tr[3]/td[1]/text()").extract(),
        self.item['commit_message'] = response.xpath("/html/body/div/div/pre/text()").extract()
        # self.item['difTree'] = response.xpath("/html/body/div/div/ul/li/a/text()").extract()
        self.item['difTree'] = []
        dif  = response.xpath("/html/body/div/div/ul/li/a/text()").extract()
        for value in dif:
            self.item['difTree'].append(value)
            pass

        yield self.item
