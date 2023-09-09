from flask import Blueprint

api = Blueprint('v1', __name__)


from . import test  # noqa
from . import student  # noqa
