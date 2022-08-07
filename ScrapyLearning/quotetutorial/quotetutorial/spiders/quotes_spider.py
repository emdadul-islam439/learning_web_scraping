import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    next_page_number = - 1
    start_urls = [
        # "http://quotes.toscrape.com/login"
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        print("in the PARSE() function...................................")
        return self.start_scraping(response)
        # item = QuotetutorialItem()
        # all_quote_card = response.css("div.quote")

        # for quote_info in all_quote_card:
        #     title = quote_info.css("span.text::text").get()
        #     author = quote_info.css("small.author::text").get()
        #     tags = quote_info.css("a.tag::text").getall()

        #     item['title'] = title
        #     item['author'] = author
        #     item['tags'] = tags
        
        #     yield item
        
        # token = response.css("input::attr(value)").get()
        # print(f"CSRF TOKEN = {token}............................")
        # FormRequest.from_response(response, formdata={
        #     'csrf_token' : token,
        #     'username' : "emdad",
        #     'password' : "hello"
        # }, callback = self.start_scraping)

    
    def start_scraping(self, response):
        print("in the start_scraping() function...................................")
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


    # def start_scraping(self, response):
    #     if QuoteSpider.next_page_number == -1:
    #         QuoteSpider.next_page_number = 1
    #         next_page = f"https://quotes.toscrape.com/page/{QuoteSpider.next_page_number}/"
    #         yield response.follow(next_page, callback = self.start_scraping)

    #     item = QuotetutorialItem()
    #     all_quote_card = response.css("div.quote")

    #     for quote_info in all_quote_card:
    #         title = quote_info.css("span.text::text").get()
    #         author = quote_info.css("small.author::text").get()
    #         tags = quote_info.css("a.tag::text").getall()

    #         item['title'] = title
    #         item['author'] = author
    #         item['tags'] = tags
        
    #         yield item

    #         next_page = f"https://quotes.toscrape.com/page/{QuoteSpider.next_page_number}/"
    #         if QuoteSpider.next_page_number < 11:
    #             QuoteSpider.next_page_number += 1
    #             yield response.follow(next_page, callback = self.start_scraping)