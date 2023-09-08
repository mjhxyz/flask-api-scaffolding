from . import api


@api.get('/test')
def test():
    """v2 测试路由"""
    return 'this is v2'
