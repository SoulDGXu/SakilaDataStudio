# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:23:48 2020

@author: Xu
案例3： 订单商品构成模型图设计
1.数据查询：
订单商品构成模型的数据模型程序，
负责从数据准备中生成的影片信息表中，
查询不同类型的影片订单量，并返回给调用程序。

2.图表创建：基本环形图


"""
import pymysql.cursors
from pyecharts.charts import Pie, Page
from pyecharts import options as opts


# 不同类型的影片订单量查询
def order_category_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句：
            sql = "select category_name as 电影类型,count(*) as 订单量 from film_information_full group by category_name "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["电影类型"])
                    dataY.append(row["订单量"])
                    # 打印结果
                    print("电影类型：%s,订单量：%d" % (row["电影类型"], row["订单量"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()



# 不同等级的影片订单量查询
def order_rating_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句：
            sql = "select rating as 电影等级,count(*) as 订单量 from film_information_full group by rating "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["电影等级"])
                    dataY.append(row["订单量"])
                    # 打印结果
                    print("电影等级：%s,订单量：%d" % (row["电影等级"], row["订单量"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()        
        
        
# 不同租赁时长的订单量查询
def order_rental_duration_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句：
            sql = "select rental_duration as 电影租赁时长,count(*) as 订单量 from film_information_full group by rental_duration "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["电影租赁时长"])
                    dataY.append(row["订单量"])
                    # 打印结果
                    print("电影租赁时长：%s,订单量：%d" % (row["电影租赁时长"], row["订单量"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()            
        
# 不同租赁价格的订单量查询
def order_rental_rate_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句：
            sql = "select rental_rate as 电影租赁价格,count(*) as 订单量 from film_information_full group by rental_rate "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["电影租赁价格"])
                    dataY.append(row["订单量"])
                    # 打印结果
                    print("电影租赁价格：%s,订单量：%d" % (row["电影租赁价格"], row["订单量"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()                
        
        


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