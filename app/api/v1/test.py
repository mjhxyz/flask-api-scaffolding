from . import api
from app.api.common.resp import Success, NotFoundError


@api.get('/test')
def test():
    return Success('this is v1')


@api.get('/test_not_found')
def test_not_found():
    return NotFoundError('没有找到 test_not_found')
