from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_text=requests.get('https://quotes.toscrape.com/').text
soup=BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())

page_title=soup.find('div', class_='col-md-8').h1.a.text
viewing_tag=soup.find('div', class_='container').h3
if viewing_tag is not None:
    with open('Quotes.txt', 'w')as f:
        f.write(f'{page_title}\n {viewing_tag.a.text.capitalize()}\n\n')
else:
    with open('Quotes.txt', 'w')as f:
        f.write(f'{page_title}\n\n')
cards=soup.find_all('div', class_='quote')

for card in cards:
    quote=card.find('span', class_='text').text
    author=card.find('small', class_='author').text
    about='https://quotes.toscrape.com/'+card.a['href']
    tags=card.find('div', class_='tags').text.split('\n')[3:-1]
    
    with open('Quotes.txt', 'a')as f:
        f.write(f'Quote: {quote}\n By: {author}\n About Author: {about}\n Tags: {tags}\n\n')    
    
    #print(f'Quote: {quote}\n By: {author}\n About Author: {about}\n Tags: {tags}\n')
print('File Saved')