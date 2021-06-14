import os

from datetime import datetime

import requests

USERNAME = 'paulaabrodrigues'
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

day = datetime(year=2021, day=12, month=6)
pixel_config = {
    'date': day.strftime("%Y%m%d"),
    'quantity': '30'
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
