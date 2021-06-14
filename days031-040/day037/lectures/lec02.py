import os
import requests

USERNAME = 'paulaabrodrigues'
TOKEN = os.getenv('PIXELA_TOKEN')

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': "Reading Tracker",
    'unit': 'pages',
    'type': 'int',
    'color': 'ajisai',
    'timezone': 'America/Sao_Paulo'
}

response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
