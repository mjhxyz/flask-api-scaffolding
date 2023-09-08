from flask import Blueprint


api = Blueprint('basic', __name__)


from . import router  # noqa
