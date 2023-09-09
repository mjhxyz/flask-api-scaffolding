# 学生处理
from app.api.common.resp import Success, NotFoundError, ClientError
from app.db.mysql_utils import db, Query
from . import api

from pypika import Table, Field, Parameter


@api.get('/student/list')
def list():
    """获取学生列表"""
    q = Query.from_('student').select('id', 'name', 'add_time', 'class_id')
    result = db.query(q.get_sql())
    return Success(result)


@api.get('/student/detail_list')
def list_detail():
    """获取学生详情列表 带班级"""
    student = Table('student')
    class_ = Table('class')
    # SELECT `student`.`id`,`student`.`name`,`student`.`add_time`,`class`.`name` `class_name` FROM `student` LEFT JOIN `class` ON `student`.`class_id`=`class`.`id`
    q = Query.from_(student).left_join(class_).on(student.class_id == class_.id).select(
        student.id, student.name, student.add_time, class_.name.as_('class_name'))
    result = db.query(q.get_sql())
    return Success(result)


@api.get('/student/trade')
def student_trade():
    """转账事务例子"""
    from_id = 1
    to_id = 2
    money = 100
    with db.transaction() as conn:
        cursor = conn.cursor(prepared=True, dictionary=True)
        # SELECT `balance` FROM `student` WHERE `id`=1 FOR UPDATE
        q = Query.from_('student').select('balance').where(
            Field('id') == from_id).for_update()
        # q = Query.from_('student').select('balance').where(
        #     Field('id') == Parameter('?')).for_update()
        # cursor.execute(q.get_sql(), (from_id,))
        cursor.execute(q.get_sql())
        result = cursor.fetchone()
        if result is None:
            raise ClientError('没有找到付款人')
        from_balance = result['balance']
        if from_balance < money:
            raise ClientError('余额不足')
        # SELECT `balance` FROM `student` WHERE `id`=2 FOR UPDATE
        q = Query.from_('student').select('balance').where(
            Field('id') == to_id).for_update()
        cursor.execute(q.get_sql())
        result = cursor.fetchone()
        if result is None:
            raise ClientError('没有找到 to_id')
        to_balance = result['balance']
        # UPDATE `student` SET `balance`=8900 WHERE `id`=1
        q = Query.update('student').set('balance', from_balance - money).where(
            Field('id') == from_id)
        # raise Exception('强行报错!')
        cursor.execute(q.get_sql())
        # UPDATE `student` SET `balance`=5100 WHERE `id`=2
        q = Query.update('student').set('balance', to_balance + money).where(
            Field('id') == to_id)
        cursor.execute(q.get_sql())
        return Success('转账成功')
