# scraped data -> item container -> Json/Csv file
# scraped data -> item container ->  pipeline ->  SQL/Mongo Database
import sqlite3
from itemadapter import ItemAdapter

class QuotetutorialPipeline:
    def __init__(self) -> None:
        self.create_connection
        self.create_db

    def create_connection(self) -> None:
        self.connection = sqlite3.connect("myquote.db")
        self.cursor = self.connection.cursor()

    def create_db(self) -> None:
        self.cursor.execute("""DROP TABLE IF EXIST quotes_table""")
        self.cursor.execute("""create table quotes_table(
            title text,
            author text,
            tags text
        )""")

    def process_item(self, item, spider):
        print(f"PipeLine--------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>> {item['title'][0]} ITEMS PRINTED..........................")
        self.store_db(item)
        return item

    def store_db(self, item) -> None:
        self.cursor.execute("""insert into quotes_table values (?, ?, ?)""", (
            item['title'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.connection.commit()