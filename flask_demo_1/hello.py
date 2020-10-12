# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:54:09 2020

@author: Xu

Flask最小的应用：hello.py
Flask 应用程序的开发，通常包括 6 个步骤：
导入模块、声明对象、路由设置、业务逻辑处理、数据逻辑处理和服务启动。


"""

# 01.导入文件
from flask import Flask
# 02.创建对象
app = Flask(__name__)

# 03.路由设置
@app.route('/')
# 04.业务逻辑
def hello():
    return '欢迎来到：Python Flask Web 框架基础理论'

# 05. 服务启动
if __name__ == '__main__':
    app.run()
