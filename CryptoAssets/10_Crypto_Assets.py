import sys
import io
sys.stdout= io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #Webdriver for Google Chrome
from selenium.webdriver.common.by import By             #For going to an element on page same as soup
from selenium.webdriver.common.keys import Keys         #For using keys like enter, shift etc.
from selenium.webdriver.support.ui import WebDriverWait #This helps to wait on the webpage for like loading the full webpage in given seconds
from selenium.webdriver.support import expected_conditions as EC    #This tells if we get the element or not after waiting and if not the program quits
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

url=r'https://coinmarketcap.com/'
html_text=requests.get(url).text
soup=BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())

title=soup.find('h1', class_='sc-f70bb44c-0 ezKcbd SummaryHeader_main-title__Y_W3w').span.text
#print(title)

crypto_table=soup.find('table', class_='sc-14cb040a-3 dsflYb cmc-table')
#print(crypto_table.prettify())
crypto_rows=crypto_table.find_all('tr')
#print(rows)

data=[]
for row in crypto_rows:
    try:
        link=row.find('a', class_='cmc-link')['href']
        #print('https://coinmarketcap.com/'+link)
        name=row.find('p', class_='sc-4984dd93-0 kKpPOn').text
        #print(name)
        price=row.find('div', class_='sc-500f568e-0 ejtlWy').text
        #print(price)
        market_cap=row.find('span', class_='sc-7bc56c81-0 dCzASk').text
        #print(market_cap)
       
        data.append([name, 'https://coinmarketcap.com'+link, price, market_cap])  
    except Exception as e:
        pass


df = pd.DataFrame(data, columns=['Crypto_Name', 'Link', 'Price', 'Market_Cap'])
df.to_csv(r'10_Crypto_Assets.csv', index=False)



