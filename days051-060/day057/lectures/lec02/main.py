import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/blog')
def home():
    data = requests.get('https://api.npoint.io/780aa5562e9f8266cc96').json()
    return render_template('index.html', posts=data)


if __name__ == '__main__':
    app.run(debug=True)
