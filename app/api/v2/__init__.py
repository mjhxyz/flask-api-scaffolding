from flask import Flask, Blueprint

api = Blueprint('v2', __name__)


from . import test  # noqa
