# flask-api-scaffolding

flask api 项目手脚架 自用 (Mysql连接版)

- [flask-api-scaffolding](#flask-api-scaffolding)
  - [项目结构](#项目结构)
  - [安装方法](#安装方法)
  - [部署方法](#部署方法)
  - [统一返回格式](#统一返回格式)
    - [返回格式](#返回格式)


## 项目结构

```bash
.
├── app
│   ├── api
│   │   ├── basic
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── utils.py
│   │   ├── common
│   │   │   ├── error.py
│   │   │   ├── __init__.py
│   │   │   ├── json_codec.py
│   │   │   └── resp.py
│   │   ├── __init__.py
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   ├── student.py
│   │   │   └── test.py
│   │   └── v2
│   │       ├── __init__.py
│   │       └── test.py
│   ├── assets
│   │   └── sql
│   │       └── test.sql
│   ├── config
│   │   ├── __init__.py
│   │   ├── secure.py
│   │   └── setting.py
│   ├── db
│   │   ├── __init__.py
│   │   └── mysql_utils.py
│   ├── __init__.py
│   ├── utils
│   │   ├── md5.py
│   │   └── token.py
│   └── wsgi.py
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```


## 安装方法

要求 `python3.7` 以上的版本

基本按照方法同 master 分支

不过, 启动之前需要配置 Mysql 数据库连接

文件 `app/config/secure.py` 中进行配置, 并且 `assets/sql` 目录下有一个 `test.sql` 文件, 用于初始化数据库


```python
# Mysql config
APP_MYSQL_HOST = '192.168.60.100'
APP_MYSQL_PORT = 3306
APP_MYSQL_USER = 'root'
APP_MYSQL_PASSWORD = '000000'
APP_MYSQL_DB = 'test'
APP_MYSQL_POOL_SIZE = 1
```


## 部署方法

同 master 分支

## 统一返回格式

### 返回格式

```json
{
    "code": 1000,
    "message": "成功",
    "data": {}
}
```

```json
{
    "code": 2002,
    "message": "Token错误",
    "data": null
}
```

- code: 业务状态码
- message: 状态描述 
- data: 业务返回数据

| code | 说明                       |
| ---- | -------------------------- |
| 1000 | 成功                       |
| 2002 | Token错误                  |
| 2003 | Token过期                  |
| 2004 | 用户或密码错误             |
| 2005 | 资源未找到                 |
| 2006 | 资源已存在                 |
| 2007 | Basic 鉴权失败             |
| 3000 | 服务器内部错误             |
| -    | 其他的可以自行按照业务添加 |

