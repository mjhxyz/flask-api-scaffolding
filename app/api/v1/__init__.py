from flask import Flask, Blueprint

api = Blueprint('v1', __name__)


from . import test  # noqa
