from flask import Blueprint, render_template
from app.models import Channel

home = Blueprint("home", __name__)


@home.route("/")
def index():
    channels = Channel.query.all()
    return render_template("home/index.html", channels=channels)


@home.route("/sobre")
def about():
    return render_template("home/about.html")
