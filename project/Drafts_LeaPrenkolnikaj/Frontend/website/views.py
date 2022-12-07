from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template("home.html")

@views.route('/reservation')
def res():
    return render_template("draft.html")