import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

req = requests.get('https://zum.com/#!/home')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

keywords = soup.select('#wrap_container > div.wrap_box > div > div.issue_keyword_wrap > div.issue_keyword_total > div.list_body > ul.rank_list.d_rank_list.d_rank_keyword_0 > li > a.d_btn_keyword.d_ready > span.keyword.d_keyword')

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
data.to_csv('zum_list.csv')
