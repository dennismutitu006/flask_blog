# to handle user requests
from flask import render_template
from app import app

@app.route('/')
def index():
    '''means all request will be handled by this function'''
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
