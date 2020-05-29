import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

req = requests.get('http://ad.search.nate.com/iframe/bizhotkwd.html?v=2')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

keywords = soup.select('a')

data = []

for item in keywords:
    data.append(
        {
            'keyword': item.text,
            'time': str(datetime.now()),
        }
    )

print(data)

data = pd.DataFrame(data)
data.to_csv('nate_list.csv')
