from . import api
from app.api.common.resp import Success, NotFoundError
from app.utils import token


@api.get('/test')
def test():
    """v1 test 测试路由"""
    return Success('this is v1')


@api.get('/test_not_found')
def test_not_found():
    """v1 返回 404 测试路由"""
    raise NotFoundError('没有找到 test_not_found')


@api.get('/test_token')
def test_token():
    """v1 生成token检查token 测试路由"""
    k = token.generate_jwt_token({'user_id': 10})
    result = token.verify_jwt_token(k)
    return Success(dict(token=k, result=result))
