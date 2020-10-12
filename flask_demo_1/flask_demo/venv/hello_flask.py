# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:02:52 2020

@author: Xu

模板使用：
1. 模板设计
2. 业务逻辑设计
3. 模板渲染

"""
# 01.导入文件
from flask import Flask, render_template
# 02.创建对象
app = Flask(__name__)
# 03.路由设置
@app.route('/')
# 04.业务逻辑
def index():
    # 变量
    my_str = '我是字符串变量'
    my_int = 8888
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int
                           )
# 05. 服务启动
if __name__ == '__main__':
    app.run(debug=True)
