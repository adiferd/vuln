# -*- coding: utf-8 -*-
import scrapy


class IssuesSpider(scrapy.Spider):
    name = "issues"
    allowed_domains = ["bugs.chromium.org"]
    start_urls = ['https://bugs.chromium.org/p/chromium/issues/list?can=1&q=Security_Severity=High&sort=id']

    def parse(self, response):
        for detail_href in response.css('.id a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(detail_href),
                                 callback=self.parse_detail_issue)
        next_page = response.css('.pagination a::attr(href)').extract()[-1] # next page link is at the end of the list
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail_issue(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_css_and_re(query, re_expression):
            result = response.css(query).re(re_expression)
            if len(result) > 0:
                return result[0]

        yield {
            'id': extract_with_css_and_re('.issuemetaheader > a::text', '\d+'),
            'title': extract_with_css('.issueheader > .h3::text'),
        }
