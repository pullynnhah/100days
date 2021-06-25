import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

with sqlite3.connect('books-collection.db') as db:
    cursor = db.cursor()
    try:
        cursor.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title varchar(250) NOT NULL UNIQUE,
            author varchar(250) NOT NULL,
            rating FLOAT NOT NULL
        )""")
    except sqlite3.OperationalError:
        print("Database Already Created!")
    else:
        db.commit()


def get_book(book_id):
    with sqlite3.connect('books-collection.db') as con:
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        book_db = cur.execute("SELECT * FROM books WHERE id = ?;", (book_id,))
        return book_db.fetchone()


@app.route('/')
def home():
    with sqlite3.connect('books-collection.db') as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        book_db = cur.execute("SELECT * FROM books;")
        books = book_db.fetchall()

    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    with sqlite3.connect('books-collection.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
                    (request.form['title'], request.form['author'], request.form['rating']))
        con.commit()
    return redirect(url_for('home'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        book_id = request.args.get('id')
        print(get_book(book_id))
        return render_template('edit.html', book=get_book(book_id))

    book_id = request.form['id']
    with sqlite3.connect('books-collection.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE books SET rating = ? WHERE id = ?", (request.form['rating'], book_id))
        con.commit()
    return redirect(url_for('home'))


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    with sqlite3.connect('books-collection.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        con.commit()
    redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
