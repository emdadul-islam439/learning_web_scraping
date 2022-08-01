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
    published = job.find("span", class_= "sim-posted").span.text.replace('\n', '')
    if 'few' in published:
        company_name = job.find("h3", class_ = "joblist-comp-name").text.replace('\n', '')
        key_skills = job.find("span", class_="srp-skills").text.replace(' ', '').replace('\n', '')

        exparience_and_location_sectionn = job.find("ul", class_="top-jd-dtl clearfix")
        experience_needed = exparience_and_location_sectionn.li.contents[1]
        job_location = exparience_and_location_sectionn.find_all("li")[1].span.text
        print(company_name)
        print(key_skills)
        print(published)
        
        print(experience_needed)
        print(job_location)
        print()

# job_description = ""