# 自定义 JSON 序列化器
from datetime import datetime
from flask.json import JSONEncoder


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(obj)
