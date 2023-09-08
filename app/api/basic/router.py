from flask import Blueprint, current_app

from . import api
from .utils import required_basic_auth
from app.api.common.resp import Success, NotFoundError

# 嵌套蓝图
router = Blueprint('router', __name__)
api.register_blueprint(router, url_prefix='/router')


def get_endpoints():
    """获取所有路由信息"""
    endpoints = {}
    for rule in current_app.url_map.iter_rules():
        endpoints[rule.rule] = (
            current_app.view_functions[rule.endpoint].__doc__ or ""
        )
    return endpoints


@router.get('/list')
@required_basic_auth
def router():
    """获取项目路由信息"""
    return Success(get_endpoints())
