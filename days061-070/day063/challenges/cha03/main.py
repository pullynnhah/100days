from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collections.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Id: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nRating: {self.rating}'


db.create_all()

book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(book)
db.session.commit()
