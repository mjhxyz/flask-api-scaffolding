from flask import Flask
from werkzeug.exceptions import HTTPException


def register_blueprint(app: Flask):
    from app.api.basic import api as basic_api
    from app.api.v1 import api as api_v1
    from app.api.v2 import api as api_v2
    app.register_blueprint(api_v1, url_prefix='/v1')
    app.register_blueprint(api_v2, url_prefix='/v2')
    app.register_blueprint(basic_api, url_prefix='/basic')


def register_error_handler(app: Flask):
    @app.errorhandler(Exception)
    def framework_error(e):
        from app.api.common.error import APIException
        from app.api.common.resp import ServerError, NotFoundError

        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            error_code = 3000
            if code == 404:
                return NotFoundError()
            return APIException(error_code, msg, None)

        # 未知错误
        app.logger.exception(e)
        if app.config['DEBUG']:
            raise e
        return ServerError()


def register_plugin(app: Flask):
    # mysql 数据库
    from app.db.mysql_utils import db
    db.init_app(app)


def register_coustom_mod(app: Flask):
    # 注册自定义模块
    from app.api.common.json_codec import MyJSONEncoder
    app.json_encoder = MyJSONEncoder


def register_logger(app: Flask):
    """注册日志规则"""
    from app.utils.logger import file_logger
    file_logger.init_app(app)


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    register_error_handler(app)
    register_plugin(app)
    register_coustom_mod(app)
    register_logger(app)

    return app
