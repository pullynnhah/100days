import requests
import pandas as pd
from bs4 import BeautifulSoup


def parse_movies(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='lister-item-content')
    movies_info = []
    for item in items:
        info = {
            'title': item.select_one('h3 a').text,
            'duration': item.find(class_='runtime').text[:-4],
            'year': item.find(class_='lister-item-year').text[1:-1]
        }
        movies_info.append(info)

    return movies_info


urls = [f'https://www.imdb.com/search/title/?groups=top_1000&count=250&start={x}' for x in range(1, 1000, 250)]

movies = []
for url in urls:
    response = requests.get(url, headers={'Accept-Language': 'en-US'})
    movies.extend(parse_movies(response.content))

movies_df = pd.DataFrame(movies)
movies_df.to_csv('top_1000.csv', sep='|', index=False)
