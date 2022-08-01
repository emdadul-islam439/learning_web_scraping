from bs4 import BeautifulSoup
import requests

## requesting to the 'timesjob' website
html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html_file)  #output: <Response [200]>
content = html_file.content
# print(content)  #not a 'prettier' HTML content

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())  #prettier output 

total_result_count = soup.find('span', id = "totolResultCountsId").text

job_card_list = soup.find("li", class_ = "clearfix job-bx wht-shd-bx")


company_name = job_card_list.find("h3", class_ = "joblist-comp-name").text
key_skills = job_card_list.find("span", class_="srp-skills").text.replace(' ', '')
published = job_card_list.find("span", class_= "sim-posted").span.text

print(company_name)
print(key_skills)
print(published)
job_description = ""
experience_needed = ""
job_location = ""