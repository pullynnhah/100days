import json
import requests


response = requests.get('https://goquotes-api.herokuapp.com/api/v1/random', params={'count': 100}).json()
quotes = {'quotes': [quote['text'] for quote in response['quotes']]}

with open('data.json', 'w') as file:
    json.dump(quotes, file, indent=4)



