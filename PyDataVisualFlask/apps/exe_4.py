# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:23:08 2020

@author: Xu

案例4的Sakila客户地理位置分布的业务逻辑程序

负责响应用户对客户地理位置的数据查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序渲染出客户地理位置分布图并返回给前端页面。

"""


# 案例4：客户地理位置分布图
from pyecharts import options as opts
from pyecharts.charts import Map
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例4：数据逻辑部分
from data_4 import *

# 第一部分：业务逻辑
# 01: 不同地区的客户数量地图渲染
def customer_order_base():
    # 不同地区的客户数量查询
    dataX, dataY = customer_sum_query()
    # 对象声明
    # 订单数据
    c = (
        Map(init_opts=opts.InitOpts(width="1200px", height="600px"))
            .add("客户数量", [list(z) for z in zip(dataX, dataY)], "world")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="客户地理位置分布图"),
                            visualmap_opts=opts.VisualMapOpts(max_=1600, split_number=8, is_piecewise=True)
                            )
    )
    return c


