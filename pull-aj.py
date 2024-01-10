import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

rss_raw = requests.get('https://www.aljazeera.com/xml/rss/all.xml').text
aj_soup = BeautifulSoup(rss_raw,'html.parser')

terms = ['Palestin','Israel','Gaza','West Bank']

d = {'title':[],'description':[],'link':[]}

for item in aj_soup.find_all('item'):
    if (any(term in item.find('title').text for term in terms)) or (any(term in item.find('description').text for term in terms)):
        d['title'].append(item.find('title').text.replace('&#039;',"'"))
        d['description'].append(item.find('description').text.replace('&#039;',"'"))
        d['link'].append(item.text.split('\n')[1])

df = pd.DataFrame(d)
df.to_csv('news.csv',index=False)