import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

keywords = soup.select('channel > item > title')
time = soup.select('channel > item > pubDate')

data = []

for item in zip(keywords, time):
    data.append(
        {
            'keyword': item[0].text,
            'time': item[1].text,
        }
    )

data = pd.DataFrame(data)
data.to_csv('google_list.csv')
