import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def sparse(self, response):
        title = response.css('title').extract()
        yield {'titletext' : title}