from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")


@views.route('/character_sheet')
def character_sheet():
    return render_template("character_sheet.html")
