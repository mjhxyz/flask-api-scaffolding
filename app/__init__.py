from flask import Flask
from werkzeug.exceptions import HTTPException


def register_blueprint(app: Flask):
    pass


def register_error_handler(app: Flask):
    pass


def register_plugin(app: Flask):
    pass


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    register_error_handler(app)
    register_plugin(app)

    return app
