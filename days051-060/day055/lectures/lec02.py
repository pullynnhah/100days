from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/bye')
def bye():
    return 'Bye!'


# /Paula/24
@app.route('/<path:name>')
def greet(name):
    return f'Hello there {name}!'


@app.route('/<name>/<int:number>')
def greeting(name, number):
    return f'Hello there {name} you are {number} years old!'


if __name__ == '__main__':
    app.run(debug=True)
