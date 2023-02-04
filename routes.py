from app import app
from flask import render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', content = 'Home Page')

@app.route('/about')
def about():
    form = forms.Form()
    return render_template('about.html', content = 'About Page', form=form)


