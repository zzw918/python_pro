# server.py
# 从wsgiref模块导入
from wsgiref.simple_server import make_server

#导入之前编写的application函数
from foo import application

#创建http服务器，ip地址为空（通过localhost访问），端口是8000，处理函数是application
http = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

#开始监听HTTP请求
http.serve_forever()

