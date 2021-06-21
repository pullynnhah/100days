import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/guess/<name>')
def guess(name):
    age = requests.get(f'https://api.agify.io/?name={name}').json()['age']
    gender = requests.get(f'https://api.genderize.io/?name={name}').json()['gender']
    return render_template('index.html', name=name.title(), age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
