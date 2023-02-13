from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/task')
def task():
    tasks = Task.query.all() 
    return render_template('task.html', content = 'Tasks', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.Task()
    if form.validate_on_submit():
        task = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task'))
    return render_template('add.html', content = 'Add new', form=form)


