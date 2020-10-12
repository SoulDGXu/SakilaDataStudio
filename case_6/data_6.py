# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:52:39 2020

@author: Xu

案例6：竞争优势多维分析图设计     
图表设计：
1. 数据查询：
    竞争优势多维分析数据查询程序负责从数据库中，查询门店的多维数据，然后返回给调用程序。
2. 图表创建：雷达图
"""

from pyecharts import options as opts
from pyecharts.charts import Radar
import pymysql


# 不同门店的年营业额

def year_store_query():
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
            sql = "select * from dm_store_all where payment_date=2005"
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
                    dataX.append(row["category"])
                    dataY1.append(row["store_1"])
                    dataY2.append(row["store_2"])
                    # 打印结果
                    print("指标类别：%s,门店1的年数据：%.2f,门店2的年数据：%.2f" % (row["category"], row["store_1"], row["store_2"]))
                return dataX, dataY1, dataY2
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    print(year_store_query())
    dataX, dataY1, dataY2 = year_store_query()
    radar = Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    radar.add_schema(schema=[
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
    radar.render('radar.html')



