from random import randint
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1, 10)
    curr_year = datetime.now().year
    return render_template('index.html', num=random_number, year=curr_year)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    data = requests.get('https://api.npoint.io/780aa5562e9f8266cc96').json()
    return render_template('blog.html', posts=data)


if __name__ == '__main__':
    app.run(debug=True)
