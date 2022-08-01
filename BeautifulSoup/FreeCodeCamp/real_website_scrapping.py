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

job_card_list = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

for job in job_card_list:
    company_name = job.find("h3", class_ = "joblist-comp-name").text.replace('\n', '')
    key_skills = job.find("span", class_="srp-skills").text.replace(' ', '').replace('\n', '')
    published = job.find("span", class_= "sim-posted").span.text.replace(' ', '').replace('\n', '')

    print(company_name)
    print(key_skills)
    print(published)
    print()

# job_description = ""
# experience_needed = ""
# job_location = ""