# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:15:45 2020

@author: Xu
案例2：历史数据趋势图
图表创建，数据发布

"""

# 文件导入
from pyecharts import options as opts
from pyecharts.charts import Line
from data_2 import order_sum_query 

# 执行主函数
if __name__ == '__main__':
    print(order_sum_query())
# 数据查询
    dataX, dataY = order_sum_query()
# 对象声明
    line = Line()
    line.add_xaxis(dataX)
    line.add_yaxis("订单量", dataY, is_smooth=True)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="日订单量历史数据趋势图"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False)
    )
    line.render( )
