import requests
from bs4 import BeautifulSoup

import pandas as pd


def clean_row(row):
    text = row.split(':')[-1]
    if text.startswith('$'):
        return int(text.replace(',', '')[1:])
    if row.endswith('%'):
        return int(text[:-1])
    return text


rows = []
for page in range(1, 35):
    print(page)
    link = f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    if page == 1:
        columns = [column.text for column in soup.find_all('th')]
    rows.extend([[clean_row(row.text) for row in body.find_all('td')] for body in soup.find('tbody').find_all('tr')])
df = pd.DataFrame(data=rows, columns=columns)
df.to_csv('pay_scale_data.csv', index=False)
