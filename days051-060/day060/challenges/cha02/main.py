import requests
from flask import Flask, render_template, request

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/a6ff5a040e0baf25233b').json()


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}')
    return '<h1>Successfully sent your message</h1>'


@app.route('/post/<int:index>')
def post(index):
    return render_template('post.html', post=posts[index])



if __name__ == '__main__':
    app.run(debug=True)
