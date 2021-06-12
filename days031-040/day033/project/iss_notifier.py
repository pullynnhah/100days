import os
import smtplib

from time import sleep
from datetime import datetime

import requests


def get_hour(time):
    return int(time.split("T")[1].split(":")[0])


def is_dark(latitude, longitude):
    url = "https://api.sunrise-sunset.org/json"

    params = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    now = datetime.now()
    sunrise = get_hour(data['results']['sunrise'])
    sunset = get_hour(data['results']['sunset'])
    return not (sunrise <= now.hour <= sunset)


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    pos = response.json()["iss_position"]
    return float(pos['latitude']), float(pos['longitude'])


def check_position(pos):
    iss_pos = iss_position()
    return abs(pos[0] - iss_pos[0]) <= 5 and abs(pos[1] - iss_pos[1]) <= 5


def send_email():
    email = os.getenv('EMAIL')
    password = os.getenv('EMAIL_PASS')
    message = "Subject:ISS 👆\n\nLook up ISS is passing you now!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=message)


def is_above(latitude, longitude):
    if check_position((latitude, longitude)) and is_dark(latitude, longitude):
        send_email()
    sleep(60)
    is_above(latitude, longitude)


LATITUDE = 51.507351
LONGITUDE = -0.127758

try:
    is_above(LATITUDE, LONGITUDE)
except KeyboardInterrupt:
    print("Bye Bye")
