from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

import os

app = Flask(import_name="main")
bootstrap = Bootstrap5(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        return render_template("success.html")
        #success()
    elif request.method == 'POST' and not form.validate_on_submit():
        return render_template("denied.html")
        #denied()
    return render_template("login.html", form=form)


@app.route('/success', methods=['POST'])
def success():
    return render_template("success.html")

@app.route('/denied', methods=['POST'])
def denied():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)