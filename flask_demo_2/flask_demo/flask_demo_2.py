# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 09:59:52 2020

@author: Xu

PyEcharts 与 Flask 的框架整合模式： 前后端分离模式
示例程序：flask_demo_2.py

"""


from flask import Flask, render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
from random import randrange

# 实例程序2：前后端分离模式
# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端分离模式"))
    )
    return c


# 03-路由设置
# 03-1-路由设置：页面路由：首页渲染
@app.route("/")
def index():
    return render_template("index.html")  

  
# 03-2-路由设置：数据服务接口-图表配置属性参数 
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()    


# 04-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5002,
            debug=True)
    