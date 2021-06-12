import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
print(data)
print(data['iss_position'])

lon = data['iss_position']['longitude']
lat = data['iss_position']['latitude']
iss_position = (lon, lat)
print(lon, lat, iss_position)
