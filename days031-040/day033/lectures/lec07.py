from datetime import datetime

import requests


def get_hour(time):
    return int(time.split("T")[1].split(":")[0])


LATITUDE = 51.507351
LONGITUDE = -0.127758
URL = "https://api.sunrise-sunset.org/json"

params = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}
response = requests.get(URL, params=params)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise, sunset)

sunrise = get_hour(data['results']['sunrise'])
sunset = get_hour(data['results']['sunset'])
print(sunrise, sunset)

now = datetime.now()

