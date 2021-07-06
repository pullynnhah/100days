from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 18)])
    submit = SubmitField('Create User')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 18)])
    submit = SubmitField('Login')


class TodoForm(FlaskForm):
    name = StringField('TODO name', validators=[DataRequired()])
    submit = SubmitField('Create TODO')


class TaskForm(FlaskForm):
    todo_id = StringField('TODO id', validators=[DataRequired()])
    desc = TextAreaField('Tasks(separated by ";")', validators=[DataRequired()])
    submit = SubmitField('Create Task')
