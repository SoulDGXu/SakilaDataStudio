# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:46:45 2020

@author: Xu
PyEcharts 与 Flask 的页面刷新机制： 定时增量更新
示例程序：flask_demo_4.py

"""

from flask import Flask, render_template
from pyecharts.charts import Line
from pyecharts import options as opts
from random import randrange
from flask.json import jsonify

# 实例程序4：定时增量更新
# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-图表对象配置项参数设置
def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="定时增量更新图表"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


# 03-路由设置
# 03-1-路由设置：页面路由：首页渲染
@app.route("/")
def index():
    return render_template("index3.html")


# 03-2-路由设置：数据-图表配置属性参数
@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()


# 03-3-路由设置：数据-图表数据属性配置项更新
idx = 9
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


# 04-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5004,
            debug=True)