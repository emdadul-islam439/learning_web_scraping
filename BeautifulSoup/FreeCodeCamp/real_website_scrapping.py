from urllib.request import Request
from bs4 import BeautifulSoup
import requests

## requesting to the 'timesjob' website
html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html_file)  #output: <Response [200]>
content = html_file.content
print(content) #not a 'prettier' HTML content

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())