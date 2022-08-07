import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title_css = response.css("title::text").get()
        title_xpath = response.xpath("//title/text()").get()

        quote_text_css = response.css("span.text::text").get()
        quote_text_xpath = response.xpath("//span[@class='text']/text()").get()

        author_css = response.css("small.author::text").get()
        author_xpath = response.xpath("//small[@class='author']/text()").get()

        next_page_url_css = response.css("li.next a::attr('href')").getall()
        next_page_url_xpath = response.xpath("//li[@class='next']/a/@href").get()

        quote_by_only_class_name_css = response.css(".text::text").get()
        quote_by_only_class_name_xpath = response.xpath("//span[@class='text']/text()").get()  #had to use the 'span' tag

        css_and_xpath_marged = response.css("li.next a").xpath("@href").get()
        xpath_and_css_marged_1 = response.xpath("//li[@class='next']").css("a::attr('href')").get()
        xpath_and_css_marged_2 = response.xpath("//li[@class='next']/a").css("a::attr('href')").get() #must have use 'a' before ""::atr"
    

        yield { 'title_css' : title_css,
                'title_xpath' : title_xpath,
                'quote_text_css' : quote_text_css,
                'quote_text_xpath' : quote_text_xpath,
                'author_css' : author_css,
                'author_xpath' : author_xpath,
                'next_page_url_css' : next_page_url_css,
                'next_page_url_xpath' : next_page_url_xpath,
                'quote_by_only_class_name_css' : quote_by_only_class_name_css,
                'quote_by_only_class_name_xpath' : quote_by_only_class_name_xpath,
                'css_and_xpath_marged' : css_and_xpath_marged,
                'xpath_and_css_marged_1' : xpath_and_css_marged_1,
                'xpath_and_css_marged_2' : xpath_and_css_marged_2 }   