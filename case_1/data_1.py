# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:38:58 2020

@author: Xu

案例1： 实时数据监控指标卡

"""

import pymysql

"""
实时数据监控指标卡的数据逻辑程序，负责从数据准备环节生成的数据日报中查询交易量、
交易额和库存量指标，并返回给调用程序。

数据逻辑代码如下：

"""


# 交易量查询
def order_sum_query():
    """
    程序实现了从交易日报表中读取当日交易量的数据，供业务逻辑调用的功能。
    
    """
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_rental_day ORDER BY 日期 DESC limit 1 "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    orderdate = row["日期"]
                    ordersum = row["订单量"]
                    # 打印结果
                    print("日期：%s,交易量：%d" % (orderdate, ordersum))
                return ordersum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 交易额查询
def pay_sum_query():
    """
    程序实现了从交易日报表中读取当日交易量的数据，供业务逻辑调用的功能。
    
    """
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_payment_day ORDER BY 日期 DESC limit 1 "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    orderdate = row["日期"]
                    paysum = row["交易额"]
                    # 打印结果
                    print("日期：%s,交易额：%d" % (orderdate, paysum))
                return paysum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 库存量查询
def inventory_sum_query():
    """
    程序实现了从交易日报表中读取当日交易量的数据，供业务逻辑调用的功能。
    
    """
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_inventory_day ORDER BY 日期 DESC limit 1 "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print("%d row(s) affected" % (row_count))
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    orderdate = row["日期"]
                    inventsum = row["库存量"]
                    # 打印结果
                    print("日期：%s,库存量：%d" % (orderdate, inventsum))
                return inventsum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    print(pay_sum_query())
    print(order_sum_query())
    print(inventory_sum_query())









