import sqlite3

connection = sqlite3.connect("myquotes.db")
cursor = connection.cursor()

cursor.execute("""create table quotes_table(
            title text,
            author text,
            tags text
            """)
            
connection.commit()
connection.close()