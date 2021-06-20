import random

from flask import Flask

app = Flask(__name__)
guess = random.randint(0, 9)

def color():
    random.choice(('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'))


@app.route('/')
def intro():
    return f'<h1 style="color: {color}">Guess a number between 0 and 9</h1>' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def check(number):
    if number < guess:
        return f'<h1 style="color: {color}">Too low, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if number > guess:
        return f'<h1 style="color: {color}">Too high, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    return f'<h1 style="color: {color}">You found me!</h1>' \
           f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == '__main__':
    app.run()
