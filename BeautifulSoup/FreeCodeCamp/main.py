from bs4 import BeautifulSoup

with open('/home/emdad439/Developing/Django Journey/Learning Web Scraping/BeautifulSoup/FreeCodeCamp/example_website.html', 'r') as html_file:
    page_content = html_file.read()
    # print(page_content)

    soup = BeautifulSoup(page_content, 'lxml')
    # print(soup.prettify())


    ## working with 'tag' contents
    # tags = soup.find_all('h5')
    # for tag in tags:
    #     print(f"tag = {tag}  ||  tag_text = {tag.text}")
    

    ## working with 'head' contents
    # head_content = soup.find('head')
    # meta_tag_list = head_content.find_all('meta')
    # print(meta_tag_list)
    # for meta_tag in meta_tag_list:
    #     print(f"meta_tag = {meta_tag}  ...||...   meta_tag_text = {meta_tag.text}")

    
    ## getting course details from 'example_website'
    course_card_content = soup.find('div', class_ = 'card')

    course_name = course_card_content.find('h5')
    course_details = course_card_content.find('p')
    course_price = course_card_content.find('a')
    
    print(f"Name: {course_name.text}\nDetails: {course_details.text}\nPrice: {course_price.text}")
