from functools import wraps

from flask import request, current_app

from app.api.common.resp import BasicAuthError
from app.utils.md5 import md5_encode


def required_basic_auth(func):
    """验证 basic 功能权限"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = request.headers.get('X-Basic-Key')
        if not key:
            raise BasicAuthError()
        config = current_app.config
        pwd = config['APP_BASE_PASSWORD']
        salt = config['APP_BASE_SALT']
        if md5_encode(key + salt) != pwd:
            raise BasicAuthError()
        return func(*args, **kwargs)
    return wrapper
