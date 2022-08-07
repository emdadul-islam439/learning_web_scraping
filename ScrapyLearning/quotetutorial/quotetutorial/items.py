# scraped data -> item container -> Json/Csv file

import scrapy

class QuotetutorialItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
