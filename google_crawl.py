import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse

req = requests.get('https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

keywords = soup.select('channel > item > title')
time = soup.select('channel > item > pubDate')

data = []

for item in zip(keywords, time):
    parseTime = parse(item[1].text)
    data.append(
        {
            'keyword': item[0].text,
            'time': parseTime,
        }
    )

data = pd.DataFrame(data)
data.to_csv('google_list.csv')
