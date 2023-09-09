# 学生处理
from . import api
from app.api.common.resp import Success
from app.db.mysql_utils import db


@api.get('/student/list')
def list():
    """获取学生列表"""
    result = db.query('select * from student')
    return Success(result)
