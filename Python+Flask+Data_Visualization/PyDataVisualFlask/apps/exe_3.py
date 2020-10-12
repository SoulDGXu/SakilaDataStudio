# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:05:00 2020

@author: Xu

案例3的Sakila订单商品构成模型的业务逻辑程序

负责响应用户对商品构成数据查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序渲染出订单商品构成图并返回给前端页面。


"""


# 案例3：订单商品构成模型
from pyecharts.charts import Pie
from pyecharts import options as opts
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例3：数据逻辑部分
from data_3 import *


# 第一部分：业务逻辑
# 01: 不同类型的影片订单量
def category_order_base():
    dataX, dataY = order_category_sum_query()
    data_pair = [list(z) for z in zip(dataX, dataY)]
    # 订单数据
    c = (
        Pie()
        .add("电影类型", data_pair)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="商品类型构成图"),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="15%",
                pos_right="-4.5%"),
        )
        .set_series_opts(label_opts= opts.LabelOpts(formatter="{b}: {c} ({d}%)"),
                            position="outside",
                            background_color = "#eee",
                            border_color="#aaa",
                            border_width=1,
                            border_radius=4
                         )
            )
    return c



