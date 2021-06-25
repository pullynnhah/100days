from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    book_str = [f'{book["title"]} - {book["author"]} - {book["rating"]}/10'
                for book in all_books]
    return render_template('index.html', books=book_str)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        all_books.append({
            'title': request.form['title'],
            'author': request.form['author'],
            'rating': request.form['rating']

        })
        print(request.form)
        print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
