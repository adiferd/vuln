import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    #start_urls = ['https://bugs.chromium.org/p/chromium/issues/list?can=1&q=Security_Severity%3DCritical+&colspec=ID+Pri+M+Stars+ReleaseBlock+Component+Status+Owner+Summary+OS+Modified&x=m&y=releaseblock&cells=ids']

    start_urls = ['http://localhost/info.php']
    # def parse(self, response):
        # for title in response.css('h2.entry-title'):
            # yield {'title': title.css('a ::text').extract_first()}

        # next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        # if next_page:
            # yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
