from . import api
from app.api.common.resp import Success, NotFoundError
from app.utils import token


@api.get('/test')
def test():
    return Success('this is v1')


@api.get('/test_not_found')
def test_not_found():
    raise NotFoundError('没有找到 test_not_found')


@api.get('/test_token')
def test_token():
    k = token.generate_jwt_token({'user_id': 10})
    result = token.verify_jwt_token(k)
    return Success(dict(token=k, result=result))
