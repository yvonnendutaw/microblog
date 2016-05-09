#!flask/bin/python
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'guest'}  # fake user
    return render_template('index.html',
#                           title='Home',
                           user=user)

# login form

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])#provides openid support

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
