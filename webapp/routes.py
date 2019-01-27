from flask import render_template, flash, redirect, url_for
from application import app
from webapp.forms import LoginForm
from webapp.forms import FeedForm
from webapp.call_function import call_function
from flask import Flask, request, render_template
import requests
import os


@app.route('/', methods=['GET', 'POST'])
def home():
    egg_filename = os.path.join(app.config['DINO_FOLDER'], 'egg.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'grassy_field.jpg')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/eat', form.user_input)
    print("not validated")
    return render_template('home.html', form=form, egg_file=egg_filename, background_image=background_file)

@app.route('/eat')
def eat(user_input):
    e = requests.get('https://frontsend.azurewebsites.net/').content
    # print(e)
    return render_template('eat.html')

@app.route('/fed')
def fed():
    return render_template('fed.html')
