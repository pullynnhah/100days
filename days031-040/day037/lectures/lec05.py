import os

from datetime import datetime

import requests

USERNAME = 'paulaabrodrigues'
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = 'graph1'

day = datetime(year=2021, day=12, month=6)
pixela_endpoint = 'https://pixe.la/v1/users'
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day.strftime("%Y%m%d")}'

pixel_config = {
    'quantity': '0'
}

response = requests.put(url=update_endpoint, json=pixel_config, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
