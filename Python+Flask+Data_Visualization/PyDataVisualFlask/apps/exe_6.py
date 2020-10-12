# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:23:34 2020

@author: Xu

案例6的Sakila竞争优势多维分析的业务逻辑程序，

负责响应用户对门店各项竞争指标的数据查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序渲染出门店竞争优势对比图并返回给前端页面。

"""

# 案例6：竞争优势多维分析图
from pyecharts import options as opts
from pyecharts.charts import Radar
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例6：数据逻辑部分
from data_6 import *



# 第一部分：业务逻辑
# 01: 不同门店的竞争优势多维分析图渲染
def year_store_order_base():
    # 不同门店的年营业额数据查询
    dataX, dataY1, dataY2 = year_store_query()
    # 对象声明
    radar = Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    radar.add_schema(
            schema=[
                    opts.RadarIndicatorItem(name="门店订单金额", max_=34000),
                    opts.RadarIndicatorItem(name="门店顾客数", max_=10000),
                    opts.RadarIndicatorItem(name="门店商品类型", max_=10000),
                    opts.RadarIndicatorItem(name="门店订单量", max_=10000)
            ],
            splitarea_opt=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),
            textstyle_opts=opts.TextStyleOpts(color="#fff"),
            )
    radar.add(series_name="Store 1", data=[list(dataY1)], linestyle_opts=opts.LineStyleOpts(color="#CD0000"),)
    radar.add(series_name="Store 2", data=[list(dataY2)], linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),)
    radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    radar.set_global_opts(
                        title_opts=opts.TitleOpts(title="2005年门店竞争优势多维分析"),
                        legend_opts=opts.LegendOpts())
    return radar




