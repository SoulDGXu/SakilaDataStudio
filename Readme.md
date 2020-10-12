# Sakila：PyEcharts & Flask集成案例

**Sakila样本数据库介绍** ：Sakila样本数据库是MySQL官方提供的一个模拟DVD租赁信息管理的数据库。

Sakila的ER图如下：

![Sakila EER Diagram](.\images\Sakila EER Diagram.png)

Sakila的业务理解，影片租赁业务的业务活动主要包括租赁活动、支付活动和归还活动。如下图：

![数据主题](.\images\数据主题.png)

本文是结合Sakila的6个案例，基于 PyEcharts + Flask + Bootstrap，采用前后端分离模式，生成一个完整的数据可视化系统。本节内容的知识结构如下图所示：

![章节知识结构](.\images\章节知识结构.png)

## 1. 运行演示

PyEcharts 与 Flask 框架整合以后，结合前面6个实战案例，可以整合出一个完整的数据可视化系统。系统运行以后的效果如下图所示：

![运行演示](.\images\运行演示.gif)

动图分别呈现了实时指标监控、历史数据变化趋势、客户地理位置分布、订单商品构成模型、门店盈利能力对比和门店多维竞争优势。我们通过一个页面导航的方式，把它们组织在一起，形成了一个完整的数据可视化系统。

## 2. 源码结构

数据可视化分析系统的开发过程，采用前后端分离的开发模式，融合前面的 6 个实战案例。其完整的源码结构如下图所示：

![数据可视化系统源码结构](.\images\数据可视化系统源码结构.png)

如上图所示，整个数据可视化系统的源码位于PyDataVisualFlask 项目下，文件夹包括：apps、data、model、static 和  templates。

- apps 是业务逻辑处理模块文件目录，
- data 是数据库操作脚本文件目录，
- model  是数据库查询模块文件目录，
- static 是资源文件目录，
- templates 是模板文件目录。

## 3. 操作流程

数据可视化系统的开发流程包括**创建一个空白项目**，**复制 PyEcharts 模板文件到项目 templates 文件目录**，**前端页面设计**，**后台应用设计**和**前后端联调**五大步骤。

完成一个图表页面的开发之后，我们会重新回到前端页面设计环节，通过循环实现新的图表页面。数据可视化系统完整的开发流程，如下图所示：

![数据可视化系统开发流程](.\images\数据可视化系统开发流程.png)

1. **创建项目**：创建一个 Flask 项目，并且创建相应的文件目录结构。
2. **模板复制**：复制 PyEcharts 的模板文件到 Flask 项目的 templates 文件夹。
3. **前端页面设计**：设计需要展示的页面布局：
   1. 导入 Echarts 图表库文件，
   2. 声明图表对象占位符，
   3. 绑定页面元素，
   4. 访问远程接口，
   5. 完成图表对象的参数设置和渲染。
4. **后台应用设计**：配置 PyEcharts 图表参数，设计客户端请求路由：
   1. 页面路由请求：完成页面内容的渲染；
   2. 数据路由请求：完成图表参数的传递。
5. **前后端联调**：一方面确保数据接口的联通，另外一方面验证功能和数据的正确性。

# 实战案例：Sakila数据可视化系统

前端页面设计部分，我们需要解决的问题是主题模板选择、导航菜单设计、图表元素设计和图表事件设计；后台应用设计部分，我们需要完成的操作包括：服务接口设计、页面请求响应设计、数据请求响应设计和异常请求处理设计。

## 1. 创建项目

1. 创建一个空白的文件夹：PyDataVisualFlask ；
2. 模板默认的访问目录是templates，故在空白文件夹下，创建一个templates文件夹，用来存放PyEcharts模板文件。

创建项目完成后的文件结构如下所示：

![创建空白项目](.\images\创建空白项目.png)

## 2. 复制模板

**复制模板**指复制 PyEcharts 模板文件到新创建的 Flask 空白项目模板文件夹中。具体的操作方式分为 2 个步骤：

1. 找到 PyEcharts 模板文件；

   1. 查找 PyEcharts 模板文件的路径，可以通过 pip show pyecharts 指令，查询其安装位置。具体的操作指令执行界面如下图所示：

      ![PyEcharts 安装目录查询](.\images\PyEcharts 安装目录查询.png)

   2. PyEcharts 的安装目录位于：D:\XuProgramFiles\Anaconda3\Lib\site-packages，在该目录下找到pyecharts文件夹下的templates文件夹，如下所示：

      ![PyEcharts 模板文件](.\images\PyEcharts 模板文件.png)

2. 复制 PyEcharts 模板文件到 Flask 空白项目（这里是PyDataVisualFlask ）的 templates 文件夹。复制后的目录结构如下图所示：
   ![项目模板文件](.\images\项目模板文件.png)

## 3. 前端页面设计

### 3.1 主题模板选择

构建基于网页的 Web 类应用系统，一般要求有美观的界面，主题分明的配色方案，清晰明了的内容组织，这样能带来良好的用户体验。通常会首选免费开源的主题模板，主题模板定义了页面的组件元素、样式和配色。本案例中，选择 Bootstrap 的主题样式模板：[Matrix Admin](https://www.matrixadmin.wrappixel.com/) 开源免费版本。其官方网站如下图所示：

![Bootstrap 主题样式文件](.\images\Bootstrap 主题样式文件.png)

Matrix Admin 分为开源版本和商业版本，开源版本的下载地址为：[http://matrixadmin.wrappixel.com/matrix-admin-package-full.zip](http://matrixadmin.wrappixel.com/matrix-admin-package-full.zip)。下载后得到matrix-admin-package-full.zip，依次解压得到matrix-admin-bt4文件。

解压顺序：

| 顺序 | 压缩包                        | 解压后                                                       |
| ---- | ----------------------------- | ------------------------------------------------------------ |
| 1    | matrix-admin-package-full.zip | matrix-admin-package-full ( matrix-admin-package.zip, matriz-admin-old.zip ) |
| 2    | matrix-admin-package.zip      | matrix-admin-package ( matrix-admin-bt4.zip, matriz-admin-old.zip ) |
| 3    | matrix-admin-bt4.zip          | matrix-admin-bt4 ( assets, dist,  html )                     |

Matrix Admin 文件解压以后的目录结构如下图所示：

![Matrix Admin 文件目录结构](.\images\Matrix Admin 文件目录结构.png)

Matrix Admin 的文件目录，共分为 3 个文件夹：asserts、dist 和 html。

- asserts 是第三方资源依赖文件目录，
- dist 存储的是页面资源文件，
- html 存储的是示例程序。

Matrix Admin 示例程序可以直接通过浏览器查看，运行效果如下：

![Matrix Admin 运行演示](.\images\Matrix Admin 运行演示.png)

上述示例程序展现了该主题模板支持的页面元素、配色方案和主题样式。我们可以通过复用其页面元素、配色方案和主题样式，结合 PyEcharts 图表设置，设计我们自己的数据可视化系统。

### 3.2 导航菜单设计

页面导航用于在各个业务模块之间进行内容切换，是多页面内容组织的一种有效方式。页面导航栏的使用，可以有效地将页面内容按照类型分组。

数据可视化系统中，按照图表类型组织内容，除实时监控数据指标卡外，一个图表类型对应一个业务场景。设计完成之后的页面导航栏，如下图所示：

![数据可视化页面导航栏](.\images\数据可视化页面导航栏.png)

具体操作：

1. 将主题模板Matrix Admin 的文件夹asserts和dist 放入创建的Flask项目（这里是PyDataVisualFlask ）的static文件夹内。

2. 复制主题模板Matrix Admin 的文件夹html里的index.html到创建的Flask项目（这里是PyDataVisualFlask ）的templates文件夹内。

3. 修改index.html源码里页面元素组件Sidebar navigation：`<div class="scroll-sidebar">...</div>`.即声明一个页面导航栏，共包括 6 个导航菜单项，每一个导航菜单项有相应的主题样式、超级链接地址、菜单标题和折叠状态。源码如下：

   ![导航栏页面实现源码](.\images\导航栏页面实现源码.png)

### 3.3 图表元素设计

**图表页面的设计包括页面元素设计和图表事件设计**。

在index.html上写入图表页面的元素设计程序。

以历史数据变化趋势图为例，图表页面元素设计的实现代码如下所示，程序声明了一个带有 ID 的占位符 div 元素，该元素通过图表事件，实现了与 PyEcharts 图表对象的绑定。

```html
<!-- ============================================================== -->
<!-- 图表可视化组件 -->
<!-- ============================================================== -->
<div class="row"  >
    <div class="col-md-12">
        <div class="card">
            <div class="card-body">
                <div class="row">
                    <!-- column -->
                    <div class="col-lg-12">
                        <div class="flot-chart" >
                            <div class="flot-chart-content" style="text-align:center;" id="map"></div>
                        </div>
                    </div>
                    <!-- column -->
                </div>
            </div>
        </div>
    </div>
</div>
```

### 3.4 图表事件设计

在index.html上写入图表页面的事件设计程序。

定义完图表页面元素之后，接下来需要设计的是**页面图表响应事件**。通过图表响应事件，实现了页面图表元素和 PyEcharts 图表对象之间的绑定，并且为图表对象的参数获取设置了远程访问接口。历史数据变化趋势图的图表事件设计源码如下所示：

```html
<!-- 历史数据变化趋势图 -->
<script>
    $(
        function () {
            var chart = echarts.init(document.getElementById('map'), 'white', {renderer: 'canvas'});
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:5000/histChart",
                dataType: 'json',
                success: function (result) {
                    chart.setOption(result);
                }
            });
        }
    )
</script>
```

 图表事件源码实现了图表对象和页面指定 ID 元素的绑定，并且通过 ajax 技术，调用服务器端接口程序：http://127.0.0.1:5000/histChart，实现了与服务器端程序的图表配置参数数据交互。

## 4. 后台应用设计

在创建的Flask项目（这里是PyDataVisualFlask ）的data文件夹，放入6个数据库操作脚本文件：`data_prepare_1.sql`，`data_prepare_2.sql`，`data_prepare_3.sql`，`data_prepare_4.sql`，`data_prepare_5.sql`，`data_prepare_6.sql`。

- data_prepare_1.sql：案例1的Sakila实时数据监控指标卡的数据库操作：基于当前订单支付、租赁、库存明细数据，要将“分钟”数据聚合成“日”数据，分别创建一个新的订单支付、租赁、库存的日汇总数据表。
- data_prepare_2.sql：案例2的Sakila历史变化趋势图的数据库操作：基于当前订单支付、租赁、库存明细数据，需要将“分钟”数据聚合成“日”数据，生成新的交易、库存、租赁的日汇总数据表。
- data_prepare_3.sql：案例3的Sakila订单商品构成模型的数据库操作：基于当前的数据表：rental，inventory，category，film，language，film_category，创建一个包含所有租赁影片的信息表，包含影片类型、影片时长、影片租赁价格、影片评价信息等字段。
- data_prepare_4.sql：案例4的Sakila客户地理位置分布的数据库操作：基于当前的数据表：address，customer，city，country，rental，创建一个包含所有客户信息的表，包含租赁 ID、租赁日期、库存 ID、归还日期、员工 ID、顾客 ID、地址 ID、详细地址、地区、城市 ID、城市名称、经纬度信息、国家 ID，国家名称。
- data_prepare_5.sql：案例5的Sakila门店盈利能力对比分布的数据库操作：基于当前的数据表：payment，staff，创建一个含有门店营业额的汇总表，包含门店的 ID、支付日期、月营业额。
- data_prepare_6.sql：案例6的Sakila竞争优势多维分析的数据库操作：基于当前的数据表：payment，staff，rental，inventory，film_category，创建一个含有门店订单金额、门店订单数量、门店顾客数量、门店影片类型的数据表。

在创建的Flask项目（这里是PyDataVisualFlask ）的model文件夹，放入6个数据逻辑程序：`data_1.py`，`data_1.py`，`data_2.py`，`data_3.py`，`data_4.py`，`data_5.py`，`data_6.py`。

- data_1.py：案例1的Sakila实时数据监控指标卡的数据逻辑程序：负责从数据准备环节生成的数据日报中查询交易量、交易额和库存量指标，并返回给调用程序。
- data_2.py：案例2的Sakila历史变化趋势图的数据查询程序，负责从数据准备中生成的影片信息表中，按日查询租赁的影片量，并返回给调用程序。
- data_3.py：案例3的Sakila订单商品构成模型的数据模型程序，负责从数据准备中生成的影片信息表中，查询不同类型的影片订单量、不同租赁时长的影片订单量、不同等级的影片订单量、不同租赁价格的影片订单量，并返回给调用程序。
- data_4.py：案例4的Sakila客户地理位置分布的数据层查询程序：负责从数据准备中生成的完整的客户信息表中，查询各国家/地区的客户数量，并返回给调用程序。
- data_5.py：案例5的Sakila门店盈利能力对比分布的数据查询程序，负责从数据准备中生成的不同日期下门店盈利能力的表中，查询门店的营业额，然后返回给调用程序。
- data_6.py：案例6的Sakila竞争优势多维分析的数据查询程序，负责从数据库中，查询门店的多维数据，然后返回给调用程序。

在创建的Flask项目（这里是PyDataVisualFlask ）的templates文件夹，添加6个自定义的模板文件：`index.html`，`index2.html`，`index3.html`，`index4.html`，`index5.html`，`index6.html`。应用程序app.py会通过函数 render_template()引入这些index.html，同时根据后面传入的参数，对html进行修改渲染。

- index.html：根目录`"/"`，实时业务指标监控的模板文件。
- index2.html：目录`"/hist"`，历史数据变化趋势的模板文件。
- index3.html：目录`"/bar"`，订单商品构成模型的模板文件。
- index4.html：目录`"/map"`，客户地理位置分布的模板文件。
- index5.html：目录`"/clusterBar"`，门店盈利能力对比的模板文件。
- index6.html：目录`"/radar"`，门店多维竞争优势的模板文件。

在创建的Flask项目（这里是PyDataVisualFlask ）的apps文件夹，写入后台应用程序`app.py`以及6个业务逻辑程序：`exe_1.py`，`exe_2.py`，`exe_3.py`，`exe_4.py`，`exe_5.py`，`exe_6.py`。

- exe_1.py：案例1的Sakila实时数据监控指标卡的业务逻辑程序，负责响应用户实时指标的查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序组装出实时指标数据并返回给前端页面。
- exe_2.py：案例2的Sakila历史变化趋势图的业务逻辑程序，负责响应用户对影片订单量的历史数据查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序渲染出历史变化趋势图并返回给前端页面。
- exe_3.py：案例3的Sakila订单商品构成模型的业务逻辑程序，负责响应用户对商品构成数据查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序渲染出订单商品构成图并返回给前端页面。
- exe_4.py：案例4的Sakila客户地理位置分布的业务逻辑程序，负责响应用户对客户地理位置的数据查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序渲染出客户地理位置分布图并返回给前端页面。
- exe_5.py：案例5的Sakila门店盈利能力对比分布的业务逻辑程序，负责响应用户对门店盈收数据查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序渲染出门店盈利能力对比图并返回给前端页面。
- exe_6.py：案例6的Sakila竞争优势多维分析的业务逻辑程序，负责响应用户对门店各项竞争指标的数据查询请求，调用数据逻辑程序。基于数据逻辑查询的结果，业务逻辑程序渲染出门店竞争优势对比图并返回给前端页面。

### 4.1 服务接口设计

服务接口设计包括**页面请求接口和数据请求接**口:

- **页面请求接口**是浏览器对应的该页面的访问地址，
- **数据请求接口**对应的是图表对象的数据请求地址。

如下图所示：

![服务接口类型](.\images\服务接口类型.png)

#### 4.1.1 页面请求设计

在创建的Flask项目（这里是PyDataVisualFlask ）的apps文件夹，修改后台应用程序`app.py`。

以实时数据监控指标卡为例，页面请求接口定义如下：

```python
# 01. 页面数据请求服务
@app.route("/")
def index():
    cur = rt_index_base()
    return render_template("index.html", curnumber=cur)
```

上述程序设置页面请求路由的同时，定义了该页面请求的业务响应逻辑，通过调用实时数据监控指标查询函数，获取实时数据监控指标，并以参数的形式传递给页面渲染函数，从而进行页面渲染。

#### 4.1.2 数据请求设计

数据请求接口设计，以历史数据变化趋势图为例，其数据请求接口设计源码如下所示：

```python
# 02. 图表数据查询
@app.route("/histChart")
def get_hist_order_chart():
    c = hist_order_base()
    return c.dump_options_with_quotes()
```

上述程序定义了一个图表数据查询接口，包括请求响应地址和业务响应逻辑两部分内容。请求响应地址与前端页面设计部分的图表事件设计相对应，来源程序`exe_2.py`，具体的数据查询函数名称为hist_order_base()，返回的内容为图表对象的配置参数，包括数据部分和非数据部分。其函数实现如下所示：

```python
# 01. 订单量历史数据变化趋势
def hist_order_base():
    dataX, dataY  = order_sum_query()
    # 订单数据
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(dataX)
        .add_yaxis("订单量", dataY, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="日订单量历史数据趋势图"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    return c

```

上述程序实现了图表对象的参数设置，并且调用数据库查询函数，来源于程序`data_2.py`，获取了订单历史数据，其实现函数为order_sum_query()。该函数从数据库中读取数据内容，并返回给调用函数。该函数的代码实现如下所示：

```python
# 交易量查询
def order_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='密码',
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
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    orderdate = row["日期"]
                    ordersum = row["订单量"]
                    # 打印结果
                    print("日期：%s,交易额：%d" % (orderdate, ordersum))
                    return ordersum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()

```

### 4.2 异常请求设计

一个线上系统，在某些特定的情况下，会出现一些异常，比如网页不存在、网络不可用等特殊情况。默认浏览器提供的异常页面并不友好，原因是无法准确地反馈给用户具体的错误原因。因此，针对常见错误和异常，我们需要自己设计异常提示程序。

在创建的Flask项目（这里是PyDataVisualFlask ）的templates文件夹，存放设计好的异常页面模板：error-403.html，error-404.html，error-405.html，error-500.html。

Flask 提供了常见异常捕获的函数和方法，通过调用该函数，可以自定义指定错误码的响应程序。具体的调用方式如下所示：

```python
# #############################  异常处理  ###########################
# 403错误
@app.errorhandler(403)
def miss(e):
    return render_template('error-403.html'), 403


# 404错误
@app.errorhandler(404)
def error(e):
    return render_template('error-404.html'), 404


# 405错误
@app.errorhandler(405)
def error(e):
    return render_template('error-405.html'), 405


# 500错误
@app.errorhandler(500)
def error(e):
    return render_template('error-500.html'), 500
```

上述程序中，我们通过在函数声明前添加装饰器的调用，实现了对于异常错误码的捕获，并且绑定了相应的异常处理函数。当对应错误码的网络访问异常发生时，会调用对应的异常处理函数，渲染对应的异常提示页面。一个自定义的异常提示页面如下图所示：

![自定义异常处理](.\images\自定义异常处理.png)

## 5. 前后端联调

需要对前端页面和后台应用程序进行检查，保持统一和同步。

增加前端页面中导航侧边菜单栏的各个跳转页面，与后台应用的页面渲染统一，更新超链接地址。

![index页面](.\images\index页面.png)

修改templates内的6个index.html模板文件的可视化图表组件：

![index2页面](.\images\index2页面.png)

![index3页面](.\images\index3页面.png)

![index4页面](.\images\index4页面.png)

![index5页面](.\images\index5页面.png)

![index6页面](.\images\index6页面.png)

## 6.其他问题

### 6.1 关于主题模板[Matrix Admin](https://www.matrixadmin.wrappixel.com/) 的使用

将主题模板内的2个文件夹assets和dist加入ststi文件夹，并修改相应的CSS设计文件。例如：

1. 对".\images\PyDataVisualFlask\static\assets\libs\flot\css\float-chart.css"文件进行修改：图表可视化组件的高度修改为800px。

   ![CSS修改1](.\images\CSS修改1.png)

2. 修改LOGO图片等。

### 6.2 关于地图Map页面渲染不出

对于客户地理位置分布的地形图无法显示，只显示了图例项。如下图所示：

![Map 地图无法显示](.\images\Map 地图无法显示.png)

解决：查看模板文件index4.html里有没有引用ECharts的Map类图的JS代码。发现原来没有添加地图类型为world的JS源码，即`<script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/world.js"></script>`。

![Map 地图无法显示-代码溯源](.\images\Map 地图无法显示-代码溯源.png)

添加地图类型为world的JS源码资源后，地图可以正常显示。

