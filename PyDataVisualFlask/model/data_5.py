# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:21:27 2020

@author: Xu

案例5：门店盈利能力对比图设计
图表设计：
1. 数据查询：
    门店盈利能力对比分布数据查询程序，
    负责从数据准备中生成的不同日期下门店盈利能力的表中，
    查询门店的营业额，然后返回给调用程序。
2. 图表创建：Bar 簇状图
    

"""
from pyecharts import options as opts
from pyecharts.charts import Bar
import pymysql



# 不同门店的月营业额
def month_store_query():
    # 数据连接
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
            sql = "select * from dm_month_store_amount "
            try:
                # 执行 SQL 语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY1 = []
                dataY2 = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["payment_date"])
                    dataY1.append(row["store_1"])
                    dataY2.append(row["store_2"])
                    # 打印结果
                    print("支付时间：%s,门店1的月营业额：%.2f,门店2的月营业额：%.2f" % (row["payment_date"], row["store_1"], row["store_2"]))
                return dataX, dataY1, dataY2
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()





# 执行主函数
if __name__ == '__main__':
    dataX, dataY1, dataY2 = month_store_query()
    bar = Bar()
    bar.add_xaxis(dataX)
    bar.add_yaxis("Store 1", dataY1)
    bar.add_yaxis("Store 2", dataY2)
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"),
                        yaxis_opts=opts.AxisOpts(type_="value"),
                        title_opts={"text":"商店盈利能力分析图","subtext":"单位（美元）"})
    bar.render('store_amount.html')
