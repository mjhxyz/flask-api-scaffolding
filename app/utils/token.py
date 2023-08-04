# token tools
import time

import jwt
from flask import current_app

from app.api.common.resp import TokenExpiredError, TokenError


def generate_jwt_token(payload) -> str:
    """Generate JWT token"""
    config = current_app.config
    secret_key = config['JWT_SECRET_KEY']
    timestamp = int(time.time()) + config['JWT_EXPIRE_TIME']
    algorithm = 'HS256'
    payload.update({'exp': timestamp})
    return jwt.encode(payload, secret_key, algorithm)


def verify_jwt_token(token) -> dict:
    """Verify JWT token"""
    config = current_app.config
    secret_key = config['JWT_SECRET_KEY']
    algorithm = 'HS256'
    try:
        return jwt.decode(token, secret_key, algorithms=[algorithm])
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError()
    except Exception:
        raise TokenError()
