from flask import Flask

from .config import SECRET_KEY
from .views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(views, url_prefix='/')

    return app
