# scraped data -> item container -> Json/Csv file
# scraped data -> item container ->  pipeline ->  SQL/Mongo Database
from itemadapter import ItemAdapter

class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print(f"PipeLine--------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>> {item['title'][0]} ")
        return item
