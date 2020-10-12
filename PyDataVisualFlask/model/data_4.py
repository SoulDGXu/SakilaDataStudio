# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:40:54 2020

@author: Xu
案例4： 客户地理位置分布图设计
数据查询：实现与 MySQL 数据库建立连接、读取数据和格式化输出

"""



from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Map

# 不同地区的客户数量查询
def customer_sum_query():
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
            sql = "select country,count(distinct rental_id) as customer_num  from dm_customer_address group by country "

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
                    dataX.append(row["country"])
                    dataY.append(row["customer_num"])
                    # 打印结果
                    print("国家/地区：%s,客户数量：%d" % (row["country"], row["customer_num"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 中国各省市的客户数量查询
def customer_china_sum_query():
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
            sql = "select district,count(distinct rental_id) as customer_num  from dm_customer_address where country='China' group by district "

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
                    dataX.append(row["district"])
                    dataY.append(row["customer_num"])
                    # 打印结果
                    print("中国省份：%s,客户数量：%d" % (row["district"], row["customer_num"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()
       
        
# 中国山东省各城市的客户数量查询
def customer_china_province_sum_query():
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
            sql = "select city,count(distinct rental_id) as customer_num  from dm_customer_address where country='China' and district='Shandong' group by city "

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
                    dataX.append(row["city"])
                    dataY.append(row["customer_num"])
                    # 打印结果
                    print("中国山东省城市：%s,客户数量：%d" % (row["city"], row["customer_num"]))
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()
               

if __name__=='__main__':
    # 不同国家地区的客户数量分布图
    print(customer_sum_query())
    dataX, dataY = customer_sum_query()
    map_chart = Map(init_opts = opts.InitOpts(width="1200px", height="600px"))
    map_chart.add("客户数量", [list(z) for z in zip(dataX, dataY)], "world")
    map_chart.set_series_opts(label_opts = opts.LabelOpts(is_show=False)) 
    map_chart.set_global_opts(title_opts = opts.TitleOpts(title = "客户地理位置分布图"),
                              visualmap_opts = opts.VisualMapOpts(max_=1600, split_number=8, is_piecewise=True),
                              )
    map_chart.render("world_customer_address.html")
    
    # 中国各省市客户数量分布图
    print(customer_china_sum_query())
    provinces = {'Fujian':'福建', 'Gansu':'甘肃', 'Guangdong':'广东', 'Hainan':'海南', 'Hebei':'河北', 
                 'Heilongjiang':'黑龙江', 'Henan':'河南', 'Hubei':'湖北', 'Hunan':'湖南', 'Inner Mongolia':'内蒙古', 
                 'Jiangsu':'江苏', 'Jiangxi':'江西', 'Jilin':'吉林', 'Liaoning':'辽宁', 'Ningxia':'宁夏', 
                 'Shandong':'山东', 'Shanxi':'山西', 'Sichuan':'四川', 'Tianjin':'天津', 'Xinxiang':'新疆', 'Zhejiang':'浙江'}
    dataX, dataY = customer_china_sum_query()
    dataX_new = [provinces[i] if i in provinces else i  for i in dataX]
    c1 = (
        Map()
        .add("客户数量", [list(z) for z in zip(dataX_new, dataY)], "china" )
        .set_series_opts(label_opts = opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts = opts.TitleOpts(title="客户地理位置分布图"),
                         visualmap_opts = opts.VisualMapOpts(max_=250, split_number=5, is_piecewise=True))
        .render("china_customer_address.html")
            )
    
    # 山东省各城市客户数量分布图
    print(customer_china_province_sum_query())
    dataX, dataY = customer_china_province_sum_query()
    cities = {'Binzhou':'滨州市', 'Dongying':'东营市', 'Junan':'济南市', 'Laiwu':'莱芜市', 'Liaocheng':'聊城市', 
             'Rizhao':'日照市', 'Weifang':'潍坊市', 'Xintai':'泰安市', 'Yantai':'烟台市'}
    dataX_new = [cities[i] if i in cities else i  for i in dataX]
    c2 = (
        Map()
        .add("客户数量", [list(z) for z in zip(dataX_new, dataY)], "山东" )
        .set_series_opts(label_opts = opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts = opts.TitleOpts(title="客户地理位置分布图"),
                         visualmap_opts = opts.VisualMapOpts(max_=35, split_number=5, is_piecewise=True))
        .render("china_shandong_customer_address.html")
        )
    
    
    
    
    
    