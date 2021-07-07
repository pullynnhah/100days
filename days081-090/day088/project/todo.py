from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, LoginManager, current_user, login_user, login_required, logout_user
from flask_bootstrap import Bootstrap

from forms import RegisterForm, LoginForm, TodoForm, TaskForm, TodoRemovalForm, TaskRemovalForm

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = '123456'

#  ------------------------------------------------- CONNECT DATABASE ------------------------------------------------ #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#  ------------------------------------------------- CONFIGURE TABLES ------------------------------------------------ #
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    todos = relationship('Todo')


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tasks = relationship('Task')


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todos.id'))


db.create_all()
# ------------------------------------------------ LOGIN CONFIGURATION ----------------------------------------------- #
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------------------------------------------- FLASK ------------------------------------------------------ #
@app.route('/')
def home():
    return render_template('home.html', logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.name = request.form.get('name')
        user.username = request.form.get('username')
        if User.query.filter_by(username=user.username).first():
            flash("Username already exists, try another one!")
            return redirect(url_for('register'))
        hash_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
        user.password = hash_password
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('todos'))
    return render_template("register.html", logged_in=current_user.is_authenticated, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('todos'))
            flash("Password doesn't match!")
            return redirect(url_for('login'))
        flash("Username doesn't exist, try creating one!")
        return redirect(url_for('register'))
    return render_template("login.html", logged_in=current_user.is_authenticated, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/edit')
@login_required
def edit():
    return render_template('edit.html', logged_in=current_user.is_authenticated)


@app.route('/create/todos', methods=['GET', 'POST'])
@login_required
def create_todos():
    form = TodoForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        if Todo.query.filter_by(user_id=current_user.id, name=name).first():
            flash("Todo already exists, try another one!")
            return redirect(url_for('create_todos'))
        todo = Todo(
            name=name,
            user_id=current_user.id
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todos'))

    return render_template('create_todos.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/create/tasks', methods=['GET', 'POST'])
@login_required
def create_tasks():
    form = TaskForm()
    if form.validate_on_submit():
        todo_id = request.form.get('todo_id')
        if not Todo.query.get(todo_id):
            flash("Todo doesn't exist, please try with an existing Todo!")
            return redirect(url_for('create_tasks'))
        for task_desc in request.form.get('desc').split(';'):
            task = Task(
                description=task_desc,
                todo_id=todo_id
            )
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('todos'))
    return render_template('create_tasks.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/delete/todos', methods=['GET', 'POST'])
@login_required
def delete_todos():
    form = TodoRemovalForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        todo = Todo.query.filter_by(user_id=current_user.id, name=name).first()
        if not todo:
            flash("Todo doesn't exists, please try with an existing one!")
            return redirect(url_for('create_todos'))
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('todos'))

    return render_template('delete_todos.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/delete/tasks', methods=['GET', 'POST'])
@login_required
def delete_tasks():
    form = TaskRemovalForm()
    if form.validate_on_submit():
        todo_id = request.form.get('todo_id')
        if not Todo.query.get(todo_id):
            flash("Todo doesn't exist, please try with an existing one!")
            return redirect(url_for('delete_tasks'))
        for task_desc in request.form.get('desc').split(';'):
            task = Task.query.filter_by(todo_id=todo_id, description=task_desc).first()
            if task is None:
                flash("Task doesn't exist, please try with an existing one!")
                return redirect(url_for('delete_tasks'))
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('todos'))
    return render_template('delete_tasks.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/todos')
def todos():
    todo_dict = {}
    todos_list = Todo.query.filter_by(user_id=current_user.id).all()
    if not todos_list:
        return render_template('todos.html', logged_in=current_user.is_authenticated, todo_dict=todo_dict)
    for todo in todos_list:
        todo_dict[(todo.id, todo.name)] = Task.query.filter_by(todo_id=todo.id).all()

    return render_template('todos.html', logged_in=current_user.is_authenticated, todo_dict=todo_dict)


@app.route('/done/<kind>/<an_id>')
def done(kind, an_id):
    if kind == 'todo':
        todo = Todo.query.get(an_id)
        todo.done = not todo.done
    else:
        task = Task.query.get(an_id)
        task.done = not task.done
    db.session.commit()
    return redirect(url_for('todos'))


if __name__ == '__main__':
    app.run(debug=True)
