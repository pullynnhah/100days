from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe Image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Number of seats', validators=[DataRequired()])
    has_toilet = SelectField("Has toilet?", choices=[False, True], validators=[DataRequired()])
    has_wifi = SelectField("Has Wifi?", choices=[False, True], validators=[DataRequired()])
    has_sockets = SelectField("Has sockets?", choices={True, False}, validators=[DataRequired()])
    can_take_calls = SelectField("Can take calls?", choices=[False, True], validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    api_key = StringField('API Key', validators=[DataRequired()])
    submit = SubmitField('Add Cafe')


class SearchForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Search Cafes')
