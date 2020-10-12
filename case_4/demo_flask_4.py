# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:47:55 2020

@author: Xu

案例4： 客户地理位置分布图设计
图表创建：客户地理位置信息分布图的绑定和渲染程序

"""

from pyecharts import options as opts
from pyecharts.charts import Map
from data_4 import customer_sum_query, customer_china_sum_query, customer_china_province_sum_query
    


# 执行主函数
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
    map_chart.render("customer_address.html")
    
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
        .set_global_opts(title_opts = opts.TitleOpts(title="中国区客户地理位置分布图"),
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
        .set_global_opts(title_opts = opts.TitleOpts(title="山东省客户地理位置分布图"),
                         visualmap_opts = opts.VisualMapOpts(max_=35, split_number=5, is_piecewise=True))
        .render("china_shandong_customer_address.html")
        )
    
        
    
    










