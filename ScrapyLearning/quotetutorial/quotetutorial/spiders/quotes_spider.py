from gc import callbacks
import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    next_page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):
        item = QuotetutorialItem()
        all_quote_card = response.css("div.quote")

        for quote_info in all_quote_card:
            title = quote_info.css("span.text::text").get()
            author = quote_info.css("small.author::text").get()
            tags = quote_info.css("a.tag::text").getall()

            item['title'] = title
            item['author'] = author
            item['tags'] = tags
        
            yield item

            next_page = f"https://quotes.toscrape.com/page/{QuoteSpider.next_page_number}/"
            if QuoteSpider.next_page_number < 11:
                QuoteSpider.next_page_number += 1
                yield response.follow(next_page, callback = self.parse)