from . import api


@api.get('/test')
def test():
    return 'this is v1'
