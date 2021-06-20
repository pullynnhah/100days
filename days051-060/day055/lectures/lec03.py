from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://www.petage.com/wp-content/uploads/2019/09/Deposit' \
           'photos_74974941_xl-2015-e1569443284386-670x627.jpg" width=200>' \
           '<img src="https://media2.giphy.com/media/BNhxS88zU2maI/giphy.gif?cid=e' \
           'cf05e47ue8drnxbr6jc0s9jr9j3iii9ry19mp8ts299wb5i&rid=giphy.gif&ct=g">'


if __name__ == '__main__':
    app.run(debug=True)
