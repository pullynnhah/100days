import atexit
import os
import pyperclip

from PIL import Image
from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField

app = Flask(__name__)

Bootstrap(app)

app.config["SECRET_KEY"] = '123456'


class ImageForm(FlaskForm):
    photo = FileField('', validators=[FileRequired(), FileAllowed(['jpeg', 'jpg'], 'RBG images only!')])
    submit = SubmitField('Compute')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ImageForm()
    if form.validate_on_submit():
        file = request.files['photo']
        filename = secure_filename(form.photo.data.filename)
        file.save(f'static/images/temp/{filename}')
        return redirect(url_for('home'))
    images = os.listdir('static/images/temp')
    image = url_for('static', filename=f'images/temp/{images[0]}' if images else 'images/rainbow.jpeg')
    img = Image.open(f'.{image}')
    new_img = img.quantize(colors=10)
    colors = new_img.getpalette()
    colors_rgb = [colors[x: x + 3] for x in range(0, 30, 3)]
    hex_colors = [f'#{r:02x}{g:02x}{b:02x}' for r, g, b in colors_rgb]
    return render_template('index.html', image=image, colors=hex_colors, form=form)


@app.route('/copy/<hex_code>')
def copy(hex_code):
    pyperclip.copy(hex_code)
    return redirect(url_for('home'))


def delete_temp():
    path = 'static/images/temp'
    files = os.listdir(f'{path}')
    if files:
        os.remove(f"{path}/{files[0]}")


if __name__ == '__main__':
    app.run(debug=True)
    atexit.register(delete_temp)
