import os

from datetime import datetime, timedelta

import requests


def get_yesterday(date):
    weekday = date.weekday()
    if weekday == 0:
        return date - timedelta(days=3)
    if weekday == 6:
        return date - timedelta(days=2)
    return date - timedelta(days=1)


def format_date(date):
    return date.strftime('%Y-%m-%d')


def get_value(data, date):
    return float(data["Time Series (Daily)"][date]["4. close"])


def get_percentage(value, previous_value):
    return (value - previous_value) * 100 / value


STOCK = "TSLA"

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv('ALPHA_KEY')
}

today = datetime.now()
yesterday_raw = get_yesterday(today)
before_yesterday_raw = get_yesterday(yesterday_raw)

yesterday = format_date(yesterday_raw)
before_yesterday = format_date(before_yesterday_raw)

response = requests.get('https://www.alphavantage.co/query', params=params).json()

yesterday_value = get_value(response, yesterday)
before_yesterday_value = get_value(response, before_yesterday)
percentage = get_percentage(yesterday_value, before_yesterday_value)

if -5 <= percentage <= 5:
    print("Get News")
