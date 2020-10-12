# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:01:30 2020

@author: Xu


"""

"""
实时数据监控指标卡的业务逻辑程序，负责响应用户实时指标的查询请求，
调用数据逻辑程序，基于数据逻辑查询的结果，业务逻辑程序组装出实时指标数据并返回给前端页面。

业务逻辑代码如下：

"""


# 01. 实时指标监控
def rt_index_base():
    paysum = pay_sum_query()  # 交易额
    ordersum = order_sum_query()   # 订单量
    inventsum = inventory_sum_query()  # 库存量

    cur = {'paysum' : paysum, 'ordersum': ordersum, 'inventsum': inventsum} 
    return cur


# 定义路由和接口设计
# 01. 实时指标监控
app.route("/")
def index():
   cur = rt_index_base()
   return render_template("dashboard.html", curnumber=cur)
