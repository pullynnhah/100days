from random import randint
from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1, 10)
    curr_year = datetime.now().year
    return render_template('index.html', num=random_number, year=curr_year)



if __name__ == '__main__':
    app.run(debug=True)
