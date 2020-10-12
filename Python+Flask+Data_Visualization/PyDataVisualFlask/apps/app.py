# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:13:47 2020

@author: Xu

app.py

后台设计：
1. 服务接口设计
1.1 页面请求设计
1.2 数据请求设计 
2. 异常请求设计


"""

from flask import Flask, render_template

from exe_1 import *
from exe_2 import *
from exe_3 import *
from exe_4 import *
from exe_5 import *
from exe_6 import *



app = Flask(__name__, template_folder="../templates", static_folder="../static")


# 第二部分：路由配置
# #############################历史数据查询###########################
# 01.实时数据监控指标卡
# 01-01 页面数据请求服务
@app.route("/")
def index():
    cur = rt_index_base()
    return render_template("index.html", curnumber=cur)

# 01-02 图表数据查询
@app.route("/Chart")
def get_chart():
    c = hist_order_base()
    return c.dump_options_with_quotes()


# 02. 历史变化趋势图
# 02-01：页面渲染  
@app.route("/hist")
def hist_order():
    cur = rt_index_base()
    return render_template("index2.html", curnumber=cur)   

# 02-02：图表数据查询
@app.route("/histChart")
def get_hist_order_chart():
    c = hist_order_base()
    return c.dump_options_with_quotes()


# 03：订单商品构成模型
# 03-01：页面渲染
@app.route("/bar")
def order_bar():
    cur = rt_index_base()
    return render_template("index3.html", curnumber=cur)


# 03-02：图表数据查询
@app.route("/barChart")
def get_order_chart():
    c = category_order_base()
    return c.dump_options_with_quotes()


# 04：地理位置分布图
# 04.01 页面渲染
@app.route("/map")
def customer_map():
    cur = rt_index_base()
    return render_template("index4.html", curnumber=cur)


# 04.02 图表数据
@app.route("/mapChart")
def get_customer_order_chart():
    c = customer_order_base()
    return c.dump_options_with_quotes()


# 05: 门店盈利能力对比分布
# 05.01 页面渲染   
@app.route("/clusterBar")
def month_store_bar():
    cur = rt_index_base()
    return render_template("index5.html", curnumber=cur)

 
# 05.02 图表数据 
@app.route("/clusterBarChart")
def get_month_store_order_chart():
    c = month_store_order_base() 
    return c.dump_options_with_quotes()


# 06: 门店竞争优势多维分析图
# 06.01 页面渲染   
@app.route("/radar")
def year_store_bar():
    cur = rt_index_base()
    return render_template("index6.html", curnumber=cur)

 
# 06.02 图表数据 
@app.route("/radarChart")
def get_year_store_order_chart():
    c = year_store_order_base() 
    return c.dump_options_with_quotes()


# #############################  异常处理  ###########################
# 403错误
@app.errorhandler(403)
def miss(e):
    return render_template('error-403.html'), 403


# 404错误
@app.errorhandler(404)
def error(e):
    return render_template('error-404.html'), 404


# 405错误
@app.errorhandler(405)
def error(e):
    return render_template('error-405.html'), 405


# 500错误
@app.errorhandler(500)
def error(e):
    return render_template('error-500.html'), 500


# 主函数
if __name__ == "__main__":
    app.run()
    # 模板更改后立即生效
    app.jinja_env.auto_reload = True
    # 代码更改后立即生效
    app.run(DEBUG=True)   # 1.0以后 debug = true不再支持

