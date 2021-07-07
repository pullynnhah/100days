from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, TextAreaField, IntegerField
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
    name = StringField('Todo name', validators=[DataRequired()])
    submit = SubmitField('Create Todo')


class TodoRemovalForm(FlaskForm):
    id = IntegerField('Todo id', validators=[DataRequired()])
    name = StringField('Todo name', validators=[DataRequired()])
    submit = SubmitField('Delete Todo')


class TaskForm(FlaskForm):
    todo_id = StringField('Todo id', validators=[DataRequired()])
    desc = TextAreaField('Tasks(separated by ";")', validators=[DataRequired()])
    submit = SubmitField('Create Task')


class TaskRemovalForm(FlaskForm):
    todo_id = IntegerField('Todo id', validators=[DataRequired()])
    desc = StringField('Tasks (separated by ";")', validators=[DataRequired()])
    submit = SubmitField('Delete Task')
