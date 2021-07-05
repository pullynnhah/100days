import random

from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import CafeForm, SearchForm

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = '123456'
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/all')
def all_cafes():
    cafes = api_all_cafes().get_json()
    return render_template('all.html', cafes=cafes['cafes'])


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        response = api_add_cafe()
        if response[1] == 403:
            render_template('add.html', form=form, error=True)
        else:
            redirect(url_for('home'))
    return render_template('add.html', form=form, error=False)


@app.route('/random')
def random_cafe():
    cafe = api_random_cafe().get_json()
    return render_template('cafe.html', cafe=cafe)


@app.route('/search', methods=['GET', 'POST'])
def search_cafe():
    form = SearchForm()
    if form.validate_on_submit():
        response = api_search().get_json()
        return render_template('search.html', is_search=False, form=form, cafes=response)
    return render_template('search.html', is_search=True, form=form)

@app.route('/cafe/<cafe_id>')
def cafe_display(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    return render_template('cafe.html', cafe=cafe)



# -------------------------------------------------- API ------------------------------------------------------------- #

# HTTP GET - Read Record
@app.route('/api/random', methods=['GET'])
def api_random_cafe():
    cafe = random.choice(db.session.query(Cafe).all())
    return jsonify(cafe.to_dict())


@app.route('/api/all', methods=['GET'])
def api_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/api/search', methods=['GET'])
def api_search():
    loc = request.form.get('location')
    cafes = db.session.query(Cafe).filter_by(location=loc).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route('/api/add', methods=['POST'])
def api_add_cafe():
    if request.form.get('api_key') == 'TopSecretAPIKey':
        cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price")
        )

        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 200
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# HTTP PUT/PATCH - Update Record
@app.route('/api/update-price/<int:cafe_id>', methods=['PATCH'])
def api_update_price(cafe_id):
    apikey = request.args.get('api-key')
    if apikey == 'TopSecretAPIKey':
        price = request.args.get('new_price')
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            cafe.coffee_price = price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# HTTP DELETE - Delete Record
@app.route('/api/report-closed/<int:cafe_id>', methods=['DELETE'])
def api_close_cafe(cafe_id):
    apikey = request.args.get('api-key')

    if apikey == 'TopSecretAPIKey':
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
