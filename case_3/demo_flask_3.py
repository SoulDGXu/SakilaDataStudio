# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:54:31 2020

@author: Xu
案例3： 订单商品构成模型图设计
图表创建：基本环形图


"""
from data_3 import order_category_sum_query, order_rating_sum_query
from data_3 import order_rental_duration_sum_query, order_rental_rate_sum_query
from pyecharts.charts import Pie, Page
from pyecharts import options as opts



def pie_donut_chart(query, series_name ) -> Pie:
    print(query)
    dataX, dataY = query
    data_pair = [list(z) for z in zip(dataX, dataY)]
    pie = Pie()
    pie.add(series_name, data_pair, radius=["40%","55%"])
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="商品类型构成图"),
        legend_opts=opts.LegendOpts(orient="vertical",
                                    pos_top="15%",
                                    pos_right="4.5%"),
                        )
    pie.set_series_opts(label_opts= opts.LabelOpts(formatter="{b}: {c} ({d}%)"),
                        position="outside",
                        background_color = "#eee",
                        border_color="#aaa",
                        border_width=1,
                        border_radius=4
                     )
    return pie
    


# 执行主函数
if __name__ == '__main__':
    page = Page(layout=Page.SimplePageLayout)
    pie_1 = pie_donut_chart(order_category_sum_query(), "电影类型")
    pie_2 = pie_donut_chart(order_rating_sum_query(), "电影等级")
    pie_3 = pie_donut_chart(order_rental_duration_sum_query(), "租赁时长")
    pie_4 = pie_donut_chart(order_rental_rate_sum_query(), "租赁价格")
    page.add(pie_1, pie_2, pie_3, pie_4)
    page.render("page_simple_layout_pie.html")
    

#if __name__ == '__main__':
#    pie = pie_donut_chart(order_category_sum_query(), "电影类型" )
#    pie.render('pie.html')
#    
