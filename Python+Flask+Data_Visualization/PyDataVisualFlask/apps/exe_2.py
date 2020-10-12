# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:00:39 2020

@author: Xu

案例2的Sakila历史变化趋势图的业务逻辑程序

负责响应用户对影片订单量的历史数据查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序渲染出历史变化趋势图并返回给前端页面。


"""
# 案例2: 历史变化趋势图
from pyecharts.charts import Line
from pyecharts  import options as opts
from pyecharts.globals import ThemeType
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例2：数据逻辑部分
from data_2 import *



# 第一部分：业务逻辑
# 01. 订单量历史数据变化趋势
def hist_order_base():
    # 数据查询
    dataX, dataY  = order_sum_query()
    # 对象声明
    # 订单数据
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(dataX)
        .add_yaxis("订单量", dataY, is_smooth=True)
        .set_global_opts(
                title_opts=opts.TitleOpts(title="日订单量历史数据趋势图"),
                yaxis_opts=opts.AxisOpts(
                        type_="value",
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                        ),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    return c

