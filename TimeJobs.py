from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')

# unfamiliar_skill=input('Give the unfamiliar skill to filter out: ').lower()
# print(f"Filtering out {unfamiliar_skill}")
#print()

jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for index, job in enumerate(jobs):
    published_on=job.find('span',class_='sim-posted').span.text
    if 'few' in published_on:
        company_name=job.find('h3',class_='joblist-comp-name').text.strip()
        skills=job.find('span',class_='srp-skills').text.strip()
        #more_info=job.find('header', class_='clearfix').h2.a['href']
        more_info=job.header.h2.a['href']
        with open(f'jobs/{index}.txt', 'w') as f:
            f.write(f'Company Name: {company_name}\n')
            f.write(f'Skills required: {skills}\n')
            f.write(f'Link for more info: {more_info}')
        print(f'File {index} Saved')
        #if unfamiliar_skill not in skills:
        #print(f'Company Name: {company_name}')
        #print(f'Skills required: {skills}')
        #print(f'Link: {more_info}')
    print()
        