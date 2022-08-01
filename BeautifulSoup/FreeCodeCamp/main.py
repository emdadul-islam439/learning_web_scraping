from bs4 import BeautifulSoup

with open('/home/emdad439/Developing/Django Journey/Learning Web Scraping/BeautifulSoup/FreeCodeCamp/example_website.html', 'r') as html_file:
    page_content = html_file.read()
    # print(page_content)

    soup = BeautifulSoup(page_content, 'lxml')
    print(soup.prettify())