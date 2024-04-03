#To avoid Unicode error 
import sys
import io
sys.stdout= io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service       #Used when visible chromedriver is used
import time

from bs4 import BeautifulSoup       #Main Library
import pandas as pd                 #For saving the data

#Visible chrome 
# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

#Headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')        # To run Chrome in headless mode
driver = webdriver.Chrome(options=options)


url=r'https://coinmarketcap.com/'
driver.get(url)                         #This will open the link

data = []  # Initialize an empty list to store data from all pages

for _ in range(5):      #Number of Pages to go
    
    # To Scroll the page completly as the data is loading then only
    current_scroll_position = driver.execute_script("return window.scrollY")    #Gives current pixel position 
    scroll_amount = 500     #Number of pixels to scroll
    for _ in range(18):     #Number of scrolls
        new_scroll_position = current_scroll_position + scroll_amount
        driver.execute_script(f"window.scrollTo(0, {new_scroll_position})")
        time.sleep(1)        #Sleeping for 1 minute after scroll to get the data load
        current_scroll_position = driver.execute_script("return window.scrollY")

    html_content = driver.page_source           #Parsing HTML
    soup=BeautifulSoup(html_content, 'lxml')    #Making Soup of HTML

    crypto_table=soup.find('table', class_='sc-14cb040a-3 dsflYb cmc-table')  #Searching for table
    if crypto_table is None:    #After 3rd page it is giving None
        crypto_table=soup.find('table', class_='sc-14cb040a-3 dsflYb cmc-table  ')
    crypto_rows=crypto_table.find_all('tr')             #List of all rows in table

    for row in crypto_rows:         #Parsing each row
        try:
            link=row.find('a', class_='cmc-link')['href']                       #Link of particular coin
            name=row.find('p', class_='sc-4984dd93-0 kKpPOn').text              #Name of coin
            price=row.find('div', class_='sc-500f568e-0 ejtlWy').text           #Current Price
            market_cap=row.find('span', class_='sc-7bc56c81-0 dCzASk').text     #Market Cap
            coin_abbreviation=row.find('p', class_='sc-4984dd93-0 iqdbQL coin-item-symbol').text    #Coin Symbol
            
            data.append([name, coin_abbreviation, 'https://coinmarketcap.com'+link, price, market_cap])        #Saving data to the lst
        
        #Handling None scenarios    
        except Exception as e:
            pass

    #Pagination
    page=soup.find('ul', class_='pagination')
    ll='https://coinmarketcap.com'+page.find('li', class_='next').a['href']     #Link for next page
    driver.get(ll)      #Open the next page

#DataFrame outside the loop to accumulate data from all pages
df = pd.DataFrame(data, columns=['Crypto_Name', 'Coin_Symbol', 'Link', 'Price', 'Market_Cap'])  #DataFrame
df.to_csv(r'Crypto_Assets.csv', index=False)        #Saving to CSV
print('Done')       #Printing Done on terminal
