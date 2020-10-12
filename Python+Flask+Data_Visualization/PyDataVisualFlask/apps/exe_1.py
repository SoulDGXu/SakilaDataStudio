# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:48:12 2020

@author: Xu

案例1：案例1的Sakila实时数据监控指标卡的业务逻辑程序

负责响应用户实时指标的查询请求，调用数据逻辑程序。
基于数据逻辑查询的结果，业务逻辑程序组装出实时指标数据并返回给前端页面。


"""


# 案例1: 实时数据监控指标卡
import sys
sys.path.append(r'E:\课程资料\【拉勾教育】数据分析与可视化\15\PyDataVisualFlask\model')
# 案例1：业务逻辑部分
from data_1 import *


# 第一部分：业务逻辑
# 01. 实时指标监控
def rt_index_base():
    paysum = pay_sum_query()
    ordersum = order_sum_query()
    inventsum = inventory_sum_query()

    cur = {'paysum' : paysum, 'ordersum': ordersum, 'inventsum': inventsum}
    return cur

