import sys
import io
from bs4 import BeautifulSoup
import requests
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_text=requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_in_India').text
soup=BeautifulSoup(html_text,'lxml')
#print(soup.encode('utf-8'))

title=soup.find('h1', class_='firstHeading mw-first-heading')
print(title.text)

table=soup.find('table',class_='wikitable sortable')
headings=table.find_all('th')
table_headings=[titles.text.strip() for titles in headings]
#print(table_headings)

data=table.find_all('tr')
all_rows=[]
for row in data[1:]:
    row_data=row.find_all('td')
    row_values=[value.text.strip() for value in row_data]
    all_rows.append(row_values)
#print(all_rows)

columns_to_delete=[1,3]
result = [[value for index, value in enumerate(sublist) if index not in columns_to_delete] for sublist in all_rows]
df=pd.DataFrame(data=result, columns=table_headings)

df.to_csv(r'IndianCompanies.csv', index=False)
print('File Saved')