from bs4 import BeautifulSoup
import requests

print("Put a skill you are unfamiliar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

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
        company_name = job.find("h3", class_ = "joblist-comp-name").text.replace('\n', '').strip()
        key_skills = job.find("span", class_="srp-skills").text.replace(' ', '').replace('\n', '')
        more_info = job.find("ul", class_ = "list-job-dtl clearfix").li.a['href']

        if unfamiliar_skill not in key_skills:
            print(f"Company Name: {company_name}")
            print(f"Required Skills: {key_skills}")
            print(f"More Info: {more_info}")
            print()