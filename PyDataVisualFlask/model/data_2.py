# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:24:57 2020

@author: Xu

案例2：历史数据趋势图
1. 数据查询
历史变化趋势图的数据查询程序，负责从数据准备中生成的影片信息表中，
按日查询租赁的影片量，并返回给调用程序。


2. 图表创建：

"""




from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Line

# 交易额查询
def pay_sum_query():
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
            # SQL 查询语句
            sql = "SELECT * FROM dm_payment_day ORDER BY 日期 DESC"

            try:
                # 执行 SQL 语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["日期"])
                    dataY.append(row["交易额"])
                    # 打印结果
                    print("日期：%s,交易额：%.2f" % (row["日期"], row["交易额"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
            
    finally:
        connection.close()
        
        
        
# 交易订单量查询
def order_sum_query():
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
            # SQL 查询语句
            sql = "SELECT * FROM dm_rental_day ORDER BY 日期 DESC"

            try:
                # 执行 SQL 语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected: " % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["日期"])
                    dataY.append(row["订单量"])
                    # 打印结果
                    print("日期：%s,订单量：%d" % (row["日期"], row["订单量"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
            
    finally:
        connection.close()
 

      

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




