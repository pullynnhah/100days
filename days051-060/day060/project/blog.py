import os
import smtplib

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/a6ff5a040e0baf25233b').json()


def send_email(message):
    email = os.getenv('EMAIL')
    password = os.getenv('EMAIL_PASS')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=message)


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', msg_sent=False)
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    email_message = f'Subject:Blog Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
    send_email(email_message)
    return render_template('contact.html', msg_sent=True)


@app.route('/post/<int:index>')
def post(index):
    return render_template('post.html', post=posts[index])


if __name__ == '__main__':
    app.run(debug=True)
