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


@app.route("/")
def home():
    return render_template("index.html", movies=Movie.query.all())


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


if __name__ == '__main__':
    app.run(debug=True)
