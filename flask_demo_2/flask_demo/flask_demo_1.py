# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:01:09 2020

@author: Xu

PyEcharts 与 Flask 的框架整合模式： 前后端混合模式
示例程序：flask_demo_1.py

"""

from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 实例程序1：前后端混合模式
# 00-设置模板文件环境变量
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar

# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端混合模式"))
    )
    return c


# 03-路由设置
@app.route("/")
def index():
    # 04-图表渲染：内置模式
    c = bar_base()
    return Markup(c.render_embed())


# 05-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001,
            debug=True)

