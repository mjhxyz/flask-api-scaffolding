# flask-api-scaffolding

flask api 项目手脚架 自用

- [flask-api-scaffolding](#flask-api-scaffolding)
  - [项目结构](#项目结构)
  - [安装方法](#安装方法)
  - [部署方法](#部署方法)
  - [统一返回格式](#统一返回格式)
    - [返回格式](#返回格式)


## 项目结构

TODO

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
curl -i http://127.0.0.1:5000

HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.7.16
Date: Fri, 08 Sep 2023 14:19:51 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 73
Connection: close

{"code": 2005, "message": "\u8d44\u6e90\u672a\u627e\u5230", "data": null}
```


## 部署方法

TODO

## 统一返回格式

### 返回格式

```json
{
    "code": 0,
    "message": "成功",
    "data": {}
}
```

```json
{
    "code": 0,
    "message": "有问题",
    "data": {}
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
| 3000 | 服务器内部错误             |
| -    | 其他的可以自行按照业务添加 |

