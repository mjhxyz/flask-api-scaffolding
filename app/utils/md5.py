# md5 工具
import hashlib


def md5_encode(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest().upper()
