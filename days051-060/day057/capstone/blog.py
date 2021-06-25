import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)
posts = [Post(data) for data in requests.get('https://api.npoint.io/780aa5562e9f8266cc96').json()]


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:post_id>')
def read_post(post_id):
    return render_template('post.html', title=posts[post_id].title, body=posts[post_id].body)


if __name__ == "__main__":
    app.run(debug=True)
