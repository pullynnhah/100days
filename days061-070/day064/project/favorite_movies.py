import os

import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fav_movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,loop.index
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned "
#                 "down by an extortionist's sniper rifle. Unable to leave or receive outside"
#                 " help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()

class RateMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g. 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")


class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


def get_movies(title):
    params = {
        'api_key': os.getenv('TMDB_KEY'),
        'query': title
    }
    response = requests.get('https://api.themoviedb.org/3/search/movie', params=params).json()
    return response['results']


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = RateMovieForm()
    movie = Movie.query.get(request.args.get('id'))
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    Movie.query.filter_by(id=request.args.get('id')).delete()
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        movies = get_movies(form.title.data)
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    movie_id = request.args.get("id")
    if movie_id is None:
        return '<h1>No movies found!</h1>'
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}',
                            params={'api_key': os.getenv('TMDB_KEY')}).json()
    new_movie = Movie(title=response['title'], year=response['release_date'][-4:], description=response['overview'],
                      img_url=f"https://image.tmdb.org/t/p/original{response['poster_path']}")
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('update', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
