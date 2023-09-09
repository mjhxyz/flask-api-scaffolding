
# Base Password 用于获取比较 hack 的数据, pwd = md5(pwd+salt)
# 默认密码 000000
APP_BASE_SALT = 'MMM'
APP_BASE_PASSWORD = 'F1B603CD1CC39807F8DD97D56ACCEE05'


# JWT config
JWT_SECRET_KEY = 'ssecretsecretsecretsecretsecretecret'
JWT_EXPIRE_TIME = 2

# Mysql config
APP_MYSQL_HOST = '192.168.60.100'
APP_MYSQL_PORT = 3306
APP_MYSQL_USER = 'root'
APP_MYSQL_PASSWORD = '000000'
APP_MYSQL_DB = 'test'
APP_MYSQL_POOL_SIZE = 1
