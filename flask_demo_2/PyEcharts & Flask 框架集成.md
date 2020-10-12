# 数据发布：PyEcharts & Flask 框架集成        

## 1. 概述

**PyEcharts & Flask 框架集成**，包括 PyEcharts 与 Flask 框架整合的两种方法和数据刷新机制。完整的知识结构如下图所示：

![知识结构图](.\images\知识结构图.png)

PyEcharts 与 Flask 整合的方式有两种：前后端混合模式和前后端分离模式。

- **前后端混合模式**是指前端页面设计和后台服务响应设计糅合在一起，页面内容的渲染由后台程序控制；
- **前后端分离模式**是指前端页面设计和后台服务响应设计解耦，各自独立开发，互不干扰，最后通过接口调用的方式，进行数据交互。

PyEcharts 和 Flask 整合后，发布的 Web 应用涉及数据刷新机制的问题，目前支持的方式包括两种：定时全量刷新和定时增量刷新。

- **定时全量刷新**是指 PyEcharts 图表数据，执行定时全量的重新读取和图表内容的重新渲染；
- **定时增量刷新**是指 PyEcharts 图表数据，执行定时指定数据项的重新读取和图表项的重新渲染。

## 2. 框架整合模式

### 2.1 前后端混合模式

#### 2.1.1 操作流程

PyEcharts 与 Flask 框架整合的前后端混合模式，其操作流程如下图所示：

![前后端混合模式操作流程](.\images\前后端混合模式操作流程.png)

- **创建项目环节**会创建一个空白的 Flask 项目，
- **复制模板环节**会复制 PyEcharts 模板文件到 Flask 项目模板文件目录 templates，
- **渲染图表环节**通过后台程序，基于 PyEcharts 模板文件，渲染可视化图表。

#### 2.1.2 创建项目

1. 创建一个空白的文件夹：flask_demo；
2. 模板默认的访问目录是templates，故在空白文件夹下，创建一个templates文件夹，用来存放PyEcharts模板文件。

创建项目完成后的文件结构如下所示：

![创建空白项目](.\images\创建空白项目.png)

#### 2.1.3 复制模板

**复制模板**指复制 PyEcharts 模板文件到新创建的 Flask 空白项目模板文件夹中。具体的操作方式分为 2 个步骤：

1. 找到 PyEcharts 模板文件；

   1. 查找 PyEcharts 模板文件的路径，可以通过 pip show pyecharts 指令，查询其安装位置。具体的操作指令执行界面如下图所示：

      ![PyEcharts 安装目录查询](.\images\PyEcharts 安装目录查询.png)

   2. PyEcharts 的安装目录位于：D:\XuProgramFiles\Anaconda3\Lib\site-packages，在该目录下找到pyecharts文件夹下的templates文件夹，如下所示：

      ![PyEcharts 模板文件](.\images\PyEcharts 模板文件.png)
   
2. 复制 PyEcharts 模板文件到 Flask 空白项目（这里是flask_demo）的 templates 文件夹。复制后的目录结构如下图所示：
 ![项目模板文件](.\images\项目模板文件.png)

#### 2.1.4 渲染图表

**前后端混合模式的图表渲染，是 Flask 应用创建过程和 PyEcharts 图表创建过程的整合**。一个简单的示例程序flask_demo_1.py如下：

1. 首先创建了一个 Flask 应用对象，
2. 设定了默认模板目录为 templates，
3. 然后定义了一个图表生成函数，接下来通过业务响应函数 index，调用图表生成函数 bar_base()，
4. 最后通过 Flask 函数 Markup()进行图表渲染。

```python
from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 实例程序1：前后端混合模式
# 00-设置模板文件环境变量
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar

# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端混合模式"))
    )
    return c


# 03-路由设置
@app.route("/")
def index():
    # 04-图表渲染：内置模式
    c = bar_base()
    return Markup(c.render_embed())


# 05-主函数
if __name__ == "__main__":
    app.run()


```

#### 2.1.5 路由设置

PyEcharts 与 Flask 整合之后的路由设置方式，完全采用的是 Flask 的路由设置方式，没有任何区别。

#### 2.1.6 运行演示

PyEcharts 与 Flask 整合之后，可以通过启动 Flask 应用程序的方式直接启动服务，然后通过浏览器进行访问。上述示例程序运行效果如下图所示：

![PyEcharts 与 Flask 整合案例运行演示](.\images\PyEcharts 与 Flask 整合案例运行演示.png)

通过上述内容，我们可以看到 PyEcharts 与 Flask 框架整合，影响到只是**业务响应环节**，在这一部分，进行 PyEcharts 图表生成，并调用 Flask 模板渲染函数进行页面渲染，其他部分相比标准的 Flask 应用程序，没有任何区别。

### 2.2 前后端分离模式

#### 2.2.1 操作流程

![前后端分离模式](.\images\前后端分离模式.png)

- **创建项目环节**会创建一个空白的 Flask 项目，
- **复制模板环节**会复制 PyEcharts 模板文件到 Flask 项目模板文件目录 templates**，**
- **前端页面设计环节**设计需要展示的页面布局，
- **图表渲染环节**配置 PyEcharts 图表参数，
- **路由设计环节**设计客户端请求路由。

创建路由和复制模板环节的操作方式与前后端混合模式完全一样。

#### 2.2.2 创建项目

1. 创建一个空白的文件夹：flask_demo；
2. 模板默认的访问目录是templates，故在空白文件夹下，创建一个templates文件夹，用来存放PyEcharts模板文件。

创建项目完成后的文件结构如下所示：

![创建空白项目](.\images\创建空白项目.png)

#### 2.2.3 复制模板

**复制模板**指复制 PyEcharts 模板文件到新创建的 Flask 空白项目模板文件夹中。具体的操作方式分为 2 个步骤：

1. 找到 PyEcharts 模板文件；

   1. 查找 PyEcharts 模板文件的路径，可以通过 pip show pyecharts 指令，查询其安装位置。具体的操作指令执行界面如下图所示：

      ![PyEcharts 安装目录查询](.\images\PyEcharts 安装目录查询.png)

   2. PyEcharts 的安装目录位于：D:\XuProgramFiles\Anaconda3\Lib\site-packages，在该目录下找到pyecharts文件夹下的templates文件夹，如下所示：

      ![PyEcharts 模板文件](.\images\PyEcharts 模板文件.png)

2. 复制 PyEcharts 模板文件到 Flask 空白项目（这里是flask_demo）的 templates 文件夹。复制后的目录结构如下图所示：
   ![项目模板文件](.\images\项目模板文件.png)



#### 2.2.4 前端页面设计

**前端页面设计**：

1. 导入 Echarts 图表库文件，
2. 声明图表对象占位符，
3. 绑定页面元素，
4. 访问远程接口，
5. 完成图表对象的参数设置和渲染。

一个典型的前端页面文件index.html示例如下图所示（index.html需要提前放入templates文件夹）：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
    <script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
</head>
<body>
    <div id="bar" style="width:1000px; height:600px;"></div>
    <script>
        $(
            function () {
                var chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
                $.ajax({
                    type: "GET",
                    url: "http://127.0.0.1:5002/barChart",
                    dataType: 'json',
                    success: function (result) {
                        chart.setOption(result);
                    }
                });
            }
        )
    </script>
</body>
</html>

```

#### 2.2.5 服务接口设计

**服务接口设计是针对前端页面的数据请求设计，该接口请求的数据为 Echarts 的图表配置参数**。具体的服务路由和响应函数如下图所示：

```python
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="Flask整合：前后端分离模式"))
    )
    return c

# 数据服务接口：图表
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()
```

当浏览器页面打开地址：http://127.0.0.1:5000/ 时，页面脚本会主动调用服务器端接口: http://127.0.0.1:5000/barChart，获取图表组件配置参数，并进行页面渲染。

#### 2.2.6 路由设计

PyEcharts 与 Flask 整合：前后端分离模式，路由设置包括两部分：

1. 页面路由请求：完成页面内容的渲染；
2. 数据路由请求：完成图表参数的传递。

完整的路由设置如下所示：

```python
# 数据服务接口：图表
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


# 首页渲染
@app.route("/")
def index():
    return render_template("index.html")
```

1. 页面路由设置了**页面根目录**的访问方式，同时绑定了业务响应函数：index()，该函数以模板页面为参数，执行了页面渲染。
2. 数据路由设置了**图表数据请求**的响应接口，并绑定了业务响应函数 get_bar_chart()。

#### 2.2.7 运行演示

PyEcharts 与 Flask 整合之后，无论是前后端混合模式还是前后端分离模式，都可以通过启动 Flask 应用程序的方式直接启动服务，然后通过浏览器进行访问。程序运行效果如下图所示：

![前后端分离模式运行演示](.\images\前后端分离模式运行演示.png)

完整的Flask应用程序flask_demo_2.py如下所示：

```python
from flask import Flask, render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
from random import randrange

# 实例程序2：前后端分离模式
# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端分离模式"))
    )
    return c


# 03-路由设置
# 03-1-路由设置：页面路由：首页渲染
@app.route("/")
def index():
    return render_template("index.html")  

  
# 03-2-路由设置：数据服务接口-图表配置属性参数 
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()    


# 04-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5002,
            debug=True)
    
```

PyEcharts 与 Flask 整合的前后端分离模式，首先是前端页面和后台服务程序之间的解耦，彼此之间约定好**数据服务接口**，即可执行前后端的各自独立开发。

这里，前端页面和后台服务的数据服务接口，前端页面index.html里定义了访问远程接口`url: "http://127.0.0.1:5002/barChart"`和对图表参数的请求，后端设置**图表数据请求**的响应接口`@app.route("/barChart")`，即完成图表参数的传递，绑定业务响应函数 get_bar_chart()。具体的http://127.0.0.1:5002/barChart存放的是图表的参数，如下所示：

![barChart图表参数传递](.\images\barChart图表参数传递.png)

**前后端分离的开发模式**，是目前主流的开发模式，可以实现并行开发，从而加快项目的开发进展。

## 3. 页面刷新机制

PyEcharts 和 Flask 整合后，如何实现页面数据的刷新。

### 3.1 定时全量更新

**定时全量更新是前端页面发起的，周期性更新整个图表内容的刷新方式，更新的内容包括整个图表的配置参数**。

**实现原理是在前端页面调用 HTML 定时器函数：setInterval()，重新发起图表配置参数的接口调用**。

定时全量更新模式下，后台应用程序不需要做出调整，只需要在前端页面增加基于定时器的调度函数。一个完整的前端页面index2.html示例程序如下图所示（index2.html需要提前放入templates文件夹）：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
    <script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
</head>
<body>
    <div id="bar" style="width:1000px; height:600px;"></div>
    <script>
        var chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
        $(
            function () {
                fetchData(chart);
                setInterval(fetchData, 2000);
            }
        );
        function fetchData() {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:5003/barChart",
                dataType: 'json',
                success: function (result) {
                    chart.setOption(result);
                }
            });
        }
    </script>
</body>
</html>

```

上述程序中，通过 HTML 函数 setInterval()，设置了一个定时器对象，每隔 2 秒钟，重新调用一次图表对象渲染函数 fetchData()，实现定时全量更新图表对象。

具体可以对比未设置定时全量更新的前端页面index.html和设置定时全量更新的前端页面index2.html的代码：

![定时全量更新-前端页面比较](.\images\定时全量更新-前端页面比较.png)

定时全量更新程序flask_demo_3.py执行的效果，可以查看下面的GIF图的动态效果。

![定时全量更新动态展示](.\images\定时全量更新动态展示.gif)

通过以上示例程序，我们可以看到**定时全量更新图表是通过前端页面设置定时器函数，定时重新访问图表配置参数接口实现的**。

定时全量更新程序flask_demo_3.py完整代码：

```python
from flask import Flask, render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
from random import randrange

# 实例程序3：定时全量更新
# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端分离模式"))
    )
    return c


# 03-路由设置
# 03-1-路由设置：页面路由：首页渲染
@app.route("/")
def index():
    return render_template("index2.html")  

  
# 03-2-路由设置：数据服务接口-图表配置属性参数 
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()    


# 04-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5003,
            debug=True)
```

### 3.2 定时增量更新

**定时增量刷新**是前端页面发起的、周期性更新整个图表内容的刷新方式，更新的内容只包括图表的数据部分。

**实现的原理是在前端页面调用 HTML 定时器函数：setInterval()，重新发起图表配置数据项参数的接口调用**。

定时增量更新模式下，需要前台页面和后台应用程序同时做出调整。一方面需要前端页面增加基于定时器的调度函数，另外一方面需要后台应用程序设置单独的增量数据服务接口。一个定时增量更新完整的前端页面index3.html示例程序如下所示（index3.html需要提前放入templates文件夹）：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
    <script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>

</head>
<body>
    <div id="bar" style="width:1000px; height:600px;"></div>
    <script>
        var chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
        var old_data = [];
        $(
            function () {
                fetchData(chart);
                setInterval(getDynamicData, 2000);
            }
        );
        // 图表渲染：初始全量获取配置参数
        function fetchData() {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:5004/lineChart",
                dataType: "json",
                success: function (result) {
                    chart.setOption(result);
                    old_data = chart.getOption().series[0].data;
                }
            });
        }
        // 增量数据：定时重置数据属性
        function getDynamicData() {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:5004/lineDynamicData",
                dataType: "json",
                success: function (result) {
                    old_data.push([result.name, result.value]);
                    chart.setOption({
                        series: [{data: old_data}]
                    });
                }
            });
        }

    </script>
</body>
</html>

```

上述程序定义了一个 HTML定时器，每隔 2 秒钟，刷新一次。刷新的过程是：重新设置 Echarts 图表对象的数据属性，其他属性如标题、工具栏、提示框等参数维持不变。

具体可以对比定时全量更新的前端页面index2.html和定时增量更新的前端页面index3.html的代码：

![定时全量-定时增量-前端页面比较](.\images\定时全量-定时增量-前端页面比较.png)

相应的，我们需要在后台应用程序中，增加 Echarts 图表配置项的数据属性查询的数据服务接口。与上述前端页面程序相对应的，后台应用服务器程序的完整的源码结构如下所示：

```python
from flask import Flask, render_template
from pyecharts.charts import Line
from pyecharts import options as opts
from random import randrange
from flask.json import jsonify

# 实例程序4：定时增量更新
# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-图表对象配置项参数设置
def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="定时增量更新图表"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


# 03-路由设置
# 03-1-路由设置：页面路由：首页渲染
@app.route("/")
def index():
    return render_template("index3.html")


# 03-2-路由设置：数据-图表配置属性参数
@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()


# 03-3-路由设置：数据-图表数据属性配置项更新
idx = 9
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


# 04-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5004,
            debug=True)
```

上述程序中，共声明了 3 个服务接口：页面渲染服务接口、Echarts 图表参数配置查询接口和 Echarts 图表数据项配置参数更新接口，并且绑定了对应的业务响应函数。

定时增量更新程序flask_demo_4.py执行的效果，可以查看下面的GIF图的动态效果。

![定时增量更新动态展示](.\images\定时增量更新动态展示.gif)

### 3.3 两种页面刷新机制式对比

| 区别     | 定时全量更新                                                 | 定时增量更新                                                 |
| -------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| 页面发起 | 前端页面发起的周期性刷新                                     | 前端页面发起的周期性刷新                                     |
| 更新内容 | 整个图表的配置参数                                           | 图表的数据部分                                               |
| 实现原理 | 在前端页面调用HTML定时器函数：setInterval()，重新发起**图表配置项参数**的接口调用。 | 在前端页面调用HTML定时器函数：setInterval()，重新发起**图表配置数据项参数**的接口调用。 |
| 后台     | 后台应用程序不需要做出调整，只需要在前端页面增加基于定时器的调度函数。 | 前台页面和后台应用程序同时做出调整：前端页面增加基于定时器的调度函数，后台应用程序设置单独的增量数据服务接口。 |

## 4. 实践中遇到的一些问题

#### 4.1 python flask 本地页面不刷新内容

在数据发布篇第1篇内容中，我尝试开发一个本地的flask小应用：hello_flask.py，最终在  http://127.0.0.1:5000/ 上得到了想要的页面效果。但是，再继续开发第二个flask小应用时，Chrome上打开  http://127.0.0.1:5000/ 显示依旧是上一个应用的页面内容，刷新页面也无法加载出新的内容。

查找资料后，有几个原因和建议：

1. 没有刷新缓存。Chrome浏览器强制刷新：浏览器强制重新从服务器请求内容。
2. 服务器没有更新。停掉服务，再重启下。
3. 服务器没有更新。开启调试，`app.run(debug=True)`
4. 默认端口5000被占用，导致启动失败。修改默认端口号，即指定一个新的端口。

这里，经过修改默认端口为5001，flask应用启动后可以加载新的页面内容。

```python
from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 实例程序1：前后端混合模式
# 00-设置模板文件环境变量
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar

# 01-创建Flask对象
app = Flask(__name__, static_folder="templates")


# 02-参数配置
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-柱状图", subtitle="Flask整合：前后端混合模式"))
    )
    return c


# 03-路由设置
@app.route("/")
def index():
    # 04-图表渲染：内置模式
    c = bar_base()
    return Markup(c.render_embed())


# 05-主函数
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001,
            debug=True)
```

![PyEcharts 与 Flask 整合案例运行演示](.\images\PyEcharts 与 Flask 整合案例运行演示.png)

#### 4.2 flask





































