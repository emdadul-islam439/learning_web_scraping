import time
from bs4 import BeautifulSoup
import requests

print("Put a skill you are unfamiliar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")


def find_job():
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    content = html_file.content

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


if __name__== '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)