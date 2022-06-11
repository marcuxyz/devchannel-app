from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route("/")
def index():
    home = 'Apenas palavras...'
    return render_template('home/index.html', home=home)

@home.route("/sobre")
def about():
    return render_template('home/about.html')
