import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        quote_card = response.xpath("//div[@class='quote']")
        # title = quote_card.
        yield {'quote_card' : quote_card}