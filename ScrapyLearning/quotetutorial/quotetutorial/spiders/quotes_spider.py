import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        quote_card = response.css("div.quote")[0]
        title = quote_card.css("span.text::text").get()
        author = quote_card.css("small.author::text").get()
        tags = quote_card.css("a.tag::text").getall()
    
        yield { 
            'title' : title,
            'author' : author,
            'tags' : tags, 
         }   