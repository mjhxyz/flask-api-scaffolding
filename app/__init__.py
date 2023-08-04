from flask import Flask
from werkzeug.exceptions import HTTPException


def register_blueprint(app: Flask):
    from app.api.v1 import api as api_v1
    from app.api.v2 import api as api_v2
    app.register_blueprint(api_v1, url_prefix='/v1')
    app.register_blueprint(api_v2, url_prefix='/v2')


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
