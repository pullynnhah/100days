from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/<name>')
def greet(name):
    return f'Hello there {name}!'

# TypeError
# @app.route('/username/<username>')
# def greeting(name):
#     return f'Hello {name}!'


# TypeError
# @app.route('/username/<name>')
# def greeting2(name):
#     return f'Hello {name + 12}!'


@app.route('/username/<name>/1')
def greeting3(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
