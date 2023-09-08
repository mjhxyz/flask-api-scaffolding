# flask-api-scaffolding

flask api 项目手脚架 自用

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
│   │   ├── common
│   │   │   ├── error.py
│   │   │   ├── __init__.py
│   │   │   └── resp.py
│   │   ├── __init__.py
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   └── test.py
│   │   └── v2
│   │       ├── __init__.py
│   │       └── test.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── secure.py
│   │   └── setting.py
│   ├── __init__.py
│   ├── utils
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

1. pip 安装依赖

```bash
pip install -r requirements.txt
```

2. 启动项目

```bash
python app.py
```

3. 检查项目是否成功运行

开启一个新的终端
```bash
echo -en "$(curl -i http://127.0.0.1:5000)"

HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.7.16
Date: Fri, 08 Sep 2023 16:13:47 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 73
Connection: close

{"code": 2005, "message": "资源未找到", "data": null}
```
```bash
curl -i http://127.0.0.1:5000/v1/test

HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.7.16
Date: Fri, 08 Sep 2023 14:22:24 GMT
Content-Type: application/json
Content-Length: 60
Connection: close

{
  "code": 1000,
  "data": "this is v1",
  "message": ""
}
```

```bash
echo -en "$(curl -H "X-Basic-Key: 000000" -i http://127.0.0.1:5000/basic/router/list)"


HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.7.16
Date: Fri, 08 Sep 2023 16:37:23 GMT
Content-Type: application/json
Content-Length: 1106
Connection: close

{
  "code": 1000,
  "data": [
    {
      "desc": null,
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/static/<path:filename>"
    },
    {
      "desc": "v1 test 测试路由",
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/v1/test"
    },
    {
      "desc": "v1 返回 404 测试路由",
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/v1/test_not_found"
    },
    {
      "desc": "v1 生成token检查token 测试路由",
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/v1/test_token"
    },
    {
      "desc": "v2 测试路由",
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/v2/test"
    },
    {
      "desc": "获取项目路由信息",
      "methods": [
        "HEAD",
        "OPTIONS",
        "GET"
      ],
      "path": "/basic/router/list"
    }
  ],
  "message": ""
}
```


## 部署方法

TODO

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

