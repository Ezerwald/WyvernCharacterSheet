from pathlib import Path

from flask import Flask, session

from character_singleton import CharacterSingleton
from .config import SECRET_KEY
from .views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(views, url_prefix='/')

    load_default_character()

    return app


# Initialize character singleton and load character data
def load_default_character():
    character_singleton = CharacterSingleton()
    character_singleton.load_character(Path('saved_characters/default_character.json'))
    print("Default character loaded")
