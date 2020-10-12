# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:23:23 2020

@author: Xu


案例5的Sakila门店盈利能力对比分布的业务逻辑程序，

负责响应用户对门店盈收数据查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序渲染出门店盈利能力对比图并返回给前端页面。


"""

# 案例5：门店盈利能力对比分布
from pyecharts import options as opts
from pyecharts.charts import Bar
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例5：数据逻辑部分
from data_5 import *

# 第一部分：业务逻辑
# 01: 不同门店的盈利能力对比图渲染
def month_store_order_base():
    # 不同门店的月营业额数据查询
    dataX, dataY1, dataY2 = month_store_query()
    # 声明对象
    bar = Bar()
    bar.add_xaxis(dataX)
    bar.add_yaxis("Store 1", dataY1)
    bar.add_yaxis("Store 2", dataY2)
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"),
                        yaxis_opts=opts.AxisOpts(type_="value"),
                        title_opts={"text":"商店盈利能力分析图","subtext":"单位（美元）"})
    return bar








