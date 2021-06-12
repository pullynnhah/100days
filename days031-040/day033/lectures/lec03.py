import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    raise Exception("Bad response from ISS API")

response = requests.get(url="http://api.open-notify.org/is-now.json")

if response.status_code != 200:
    raise Exception("Bad response from ISS API")
