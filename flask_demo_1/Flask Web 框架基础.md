# 数据发布：Flask Web 框架基础 

 在前面的6个PyEcharts 图表设计的典型案例中遵循的数据分析和可视化的操作流程如下所示，但是各个案例输出的都是一个单独的图表页面，并没有组成一个完整的报表体系。这就需要**数据发布**模块的工作：整合 6 大案例的输出结果，最终生成一个完整的数据报表系统。

![操作流程](.\images\操作流程.png)

数据发布篇的内容包括：

- Python Flask Web 框架基础
- PyEcharts 与 Flask 框架集成
- PyEcharts 与 Flask 集成案例


Python Flask Web 框架基础的知识结构图如下：

![知识结构图](.\images\知识结构图.png)

## 1. Flask简介

Flask 是一个用 Python 语言开发的、轻量级的、可扩展的 Web 应用程序框架，它基于 Werkzeug WSGI 工具包和 Jinja2 模板引擎进行封装和拓展。Werkzeug WSGI 提供了路由处理、请求和响应封装，Jinja2 则提供模板文件处理。

Flask 是 Python 语言三大主流开发框架之一，另外两个分别为 Django 和 Pyramid。

## 2. Flask主要特性

Flask 具有**轻量级**和**模块化设计**的特点，其初衷就是为各种复杂的 Web 应用程序构建坚实的基础，让开发者可以自由地插入任何扩展，也可以自由地构建自己的模块。其主要特性包括 4 个方面：

- **轻量级的体系结构**：核心功能框架提供路由请求处理、请求和响应封装和模板引擎。
- **基于插件的拓展体系**：核心功能之外，一切皆插件。Flask 还具有丰富的插件资源，如 ORM、表单、权限等。
- **完善的用户文档体系**：从安装部署、项目创建、路由设置到视图设计，Flask 提供了完善的用户文档教程。
- **技术社区活跃**：作为一个开源项目，其技术社区的活跃程度，一方面代表该项目的受欢迎程度，另一方面则代表该项目的生存状态。Flask 的技术社区具有非常高的社区活跃度，表明了该项目欣欣向荣。

## 3. Flask官网

Flask 官方网站提供了丰富的学习资源，包括：文档、教程和案例。

Flask英文官网：https://palletsprojects.com/p/flask/

Flask英文用户教程：https://flask.palletsprojects.com/en/1.1.x/

Flask中文用户教程：https://dormousehole.readthedocs.io/en/latest/


## 4. Flask体系结构

![Flask 工作流程](.\images\Flask 工作流程.png)

- 客户端（通常为浏览器）发送 HTTP 请求，WEB服务器在一个网络地址的指定端口上等待接收；
- 一旦收到，会将请求通过 WSGI 交给 Application 应用处理，Application 应用就是 Flask 框架编写的应用；
- Application应用服务器对消息处理后，再通过 WSGI 返回 HTTP 响应给 WEB服务器，由WEB服务器发送给客户端。

 Flask 核心部分的体系结构，具体的内容如下所示：

![Flask 体系结构](.\images\Flask 体系结构.png)

- **路由处理**模块负责客户端请求的分发；
- **请求处理**负责客户端 HTTP 请求的接收和自定义业务逻辑的调度；
- **自定义业务逻辑**是基于 Flask 框架，用户自定义的业务处理程序；
- **模板引擎**是执行页面渲染时用到的基本框架；
- **拓展插件**用于拓展基本 Flask 框架的处理能力，如数据库访问插件 Flask-SQLAlchemy，它是对数据库访问操作的抽象，让开发者不用直接和 SQL 语句打交道；通过 Python 对象操作数据库，在舍弃一些性能开销的同时，换来的是开发效率的较大提升，和多源异构数据源的支持。

## 5. Flask源码资源

Flask 是一个开源项目，其源码资源托管在 GitHub，源码地址：https://github.com/pallets/flask/ 。

![Flask 源码资源](.\images\Flask 源码资源.png)

src/flask 目录是 Flask 框架源码程序，examples 目录是示例程序，docs 目录是文档文件，test 目录是测试用例。


## 6. Flask安装部署

通常它支持两种安装方式：pip 资源库安装和源码安装。

1. pip 资源库的安装方式：直接通过指令 pip install –U flask 完成安装。安装完成以后可以通过：pip show flask，查看安装结果。命令执行结果如下所示：

![Flask 安装验证](.\images\Flask 安装验证.png)

2. 基于源码的安装方式：从 GitHub 下载源码到本地目录，解压缩以后，进入根目录，执行安装指令：python setup.py。安装完成后，可以通过同样的方法查看是否安装成功。

## 7. Flask常用插件

Flask 的主要特点之一就是插件拓展机制，我们可以通过 Flask 的安装资源库，查找可用的 Flask 插件资源，查询地址为：https://pypi.org/search/?c=Framework+%3A%3A+Flask。查询页面如下：

![Flask 插件资源](.\images\Flask 插件资源.png)

实践中 Flask 常用的插件资源和功能的清单：

![Flask常用插件清单](.\images\Flask常用插件清单.png)

上述插件可以直接使用到我们的项目开发中，通过插件集成，可以快速地构建一个完整的 Web 应用程序，从而避免重复的造轮子的工作。


## 8. Flask入门实例

### 8.1 概述

Flask 应用程序的开发，通常包括 6 个步骤：**导入模块、声明对象、路由设置、业务逻辑处理、数据逻辑处理和服务启动**。具体的流程如下图所示：

![Flask 程序设计流程](.\images\Flask 程序设计流程.png)

- **导入模块**环节负责导入 Flask 应用程序需要类和函数；
- **对象声明**环节声明一个 Flask Application 应用对象；
- **路由设置**环节定义一个服务接口，接受来自客户端的数据请求；
- **业务响应**环节定义服务于客户端请求的业务逻辑处理，包括数据访问、加工处理和图表页面渲染等；
- **数据处理**环节定义数据库访问操作；
- **服务启动**环节启动定义好的 Flask Application 应用程序。

### 8.2 实例1-1

来源于Flask中文用户手册的一个最小应用：https://dormousehole.readthedocs.io/en/latest/quickstart.html#quickstart。

下面先了解一个最基本的 Flask 应用程序的结构：

```python
# 01.导入文件
from flask import Flask
# 02.创建对象
app = Flask(__name__)

# 03.路由设置
@app.route('/')
# 04.业务逻辑
def hello():
    return '欢迎来到：Python Flask Web 框架基础理论'

# 05. 服务启动
if __name__ == '__main__':
    app.run()

```

上述示例程序:

1. 导入了 Flask 模块，

2. 声明了一个 Flask 应用程序对象，通过调用 Flask 构造函数进行初始化，使用当前模块（__name __）的名称作为参数。

3. 通过调用 route()函数设置路由。Flask 类的 route()函数是一个装饰器，它告诉应用程序哪个 URL 应该调用那个相关的函数。本例中实现的是路由“/”和函数 hello()的绑定。

4. 通过调用 Flask 的 run()方法，在本地服务器启动一个 Flask 应用程序。Flask 应用服务器启动以后，我们在浏览器中输入地址：  http://127.0.0.1:5000/ 后，返回一个字符串：“欢迎来到：Python Flask Web  框架基础理论”。程序运行后的截图如下所示：

   ![Flask 示例程序](.\images\Flask 示例程序.png)

   python 里运行后显示：

   ![Flask 运行结果](.\images\Flask 运行结果.png)

了解了一个最基本的 Flask 应用程序的结构之后，我们就可以基于实际业务需要，进行应用服务器功能的扩展了。接下来，我们来重点看一下 Flask 模板使用。

### 8.3 Flask模板

上面的例子中，**客户端请求业务响应函数，其主要作用是生成客户端请求的响应，返回一个字符串**，这是最简单使用场景。

**实际上，业务响应函数有两个作用**：**业务逻辑处理和响应内容生成**。工程实践时，在大型 Web 应用中，把业务逻辑、表现内容放在一起，会增加代码的复杂度和维护成本，因此通常采用 **MVC 的架构模式**：

- M 代表模型，负责数据逻辑处理；
- V 代表视图，负责表现内容的处理；
- C 代表控制，负责业务逻辑的处理。

**模板是用来衔接视图表现和控制逻辑的一种实现方式**。它是一个包含响应文本的文件，包括静态内容和动态内容两部分，动态内容以变量的方式存在，它负责告诉模板引擎其具体的值，这个值需要从数据中动态地获取。

模板实现了静态内容和动态内容的结合。设计完模板以后，使用真实值替换变量，再返回最终得到的字符串内容的过程，就是页面渲染的过程。

![Flask响应函数关系](.\images\Flask模板关系.png)

**我们可以通过使用模板，实现了展示逻辑和控制逻辑的解耦**。

Flask 模板的使用包括 3 个步骤：**模板设计**、**业务逻辑设计**和**模板渲染**。

### 8.4 实例1-2

#### 8.4.1 虚拟环境

我这里创建了一个虚拟环境：

- 创建一个项目文件夹flask_demo，然后创建一个虚拟环境。创建完成项目文件夹后会有一个venv文件夹。

- 在Window 7下，开始工作前，先激活相应的虚拟环境。激活后，你的终端提示符会显示虚拟环境的名称：

  ```
  .\images\flask_demo> py -3 -m venv venv
  .\images\flask_demo> venv\Scripts\activate
  (venv).\images\flask_demo> _（光标闪动）
  ```

#### 8.4.2 Flask应用开发

在实例1-1的基础上，结合模板使用，基于实际业务需要，进行应用服务器功能的扩展。

1. 模板设计：定义一个典型的模板设计，如下所示的hello.html，将文件放入文件夹templates：

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Flask 模板演示示例</title>
   </head>
   <body>
     Flask 模板 HTML 内容：
     <br />{{ my_str }}
     <br />{{ my_int }}
   </body>
   </html>
   
   ```
   这里我的目录结构如下：

   ![虚拟环境下的目录](.\images\虚拟环境下的目录.png)

2. 业务逻辑设计：定义业务逻辑程序hello_flask.py，如下所示，这里index()函数，即业务逻辑处理函数。该函数中声明了一个字符串变量和一个整数变量，并通过函数 render_template()进行了模板渲染。

   ```python
   # 01.导入文件
   from flask import Flask, render_template
   # 02.创建对象
   app = Flask(__name__)
   # 03.路由设置
   @app.route('/')
   # 04.业务逻辑
   def index():
       # 变量
       my_str = '我是字符串变量'
       my_int = 8888
       return render_template('hello.html',
                              my_str=my_str,
                              my_int=my_int
                              )
   # 05. 服务启动
   if __name__ == '__main__':
       app.run(debug=True)
   
   ```

3. 模板渲染：hello.html里通过{{}}嵌入变量内容，渲染时变量内容会被替换成实际值。

   在虚拟环境venv下启动服务，Flask应用程序服务启动后如下：

   ![Flask应用程序启动](.\images\Flask应用程序启动.png)
   
   以上程序执行以后的输出结果如下所示：
   
   ![Flask 模板运行演示](.\images\Flask 模板运行演示.png)



### 8.5 实践中的一些问题

#### 8.5.1 渲染模板：**模板的默认访问目录`templates`**

使用 [`render_template()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.render_template) 方法可以渲染模板，你只要提供模板名称和需要作为参数传递给模板的变量就行了。下面是一个简单的模板渲染例子:

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask**模板的默认访问目录**是 `templates` 文件夹，如果使用自定义的模板（HTML文件），需要新建`templates` 文件夹，再将自定义模板文件放入。因此，如果你的应用是一个模块， 那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面：

**情形 1** : 一个模块:

```
/application.py
/templates
    /hello.html
```

**情形 2** : 一个包:

```
/application
    /__init__.py
    /templates
        /hello.html
```

#### 8.5.2  flask应用启动：`FLASK_APP`环境变量

参考https://foofish.net/flask_app.html

可以使用flask命令或python 的 `-m` 开关来运行这个应用。在Windows下，Command Prompt下，必须设置环境变量`FLASK_APP`（`FLASK_APP`用来说明Flask实例对象 app 所在的模块位置），例如我把 app 写在hello_flask.py里。

```
# windows
set FLASK_APP=hello_flask.py
# linux
export FLASK_APP=hello_flask.py
```

如果你没有指定`FLASK_APP`环境变量，flask 运行的时候首先会尝试自动去项目的根目录下的 `wsgi.py` 文件 或者 `app.py` 文件里面去找。

没找到就会报 NoAppException 错误。

具体地，在Windows下，Command Prompt下，两个方式运行应用：

1. 使用flask命令：

```
   C:\path\to\app>set FLASK_APP=hello_flask.py
   C:\path\to\app>flask run
   * Running on http://127.0.0.1:5000/
```

2. 使用python -m flask：

```
   C:\path\to\app>set FLASK_APP=hello_flask.py
   C:\path\to\app>python -m flask run
   * Running on http://127.0.0.1:5000/
```

   `C:\path\to\app`是Flask实例对象 app 所在的位置，我这里是.\images\flask_demo\venv。

#### 8.5.3 flask应用启动：`FLASK_ENV` 环境变量

参考：

https://foofish.net/flask_env.html

https://dormousehole.readthedocs.io/en/latest/quickstart.html#id10

虽然 **flask** 命令（如上8.5.2）可以方便地启动一个本地开发服务器，但是每次应用代码修改之后都需要手动重启服务器。这样不是很方便， Flask 可以做得更好。如果你打开 调试模式，那么服务器会在修改应用代码之后自动重启，并且当应用出错时还会提供一个 有用的调试器。

如果需要打开所有开发功能（包括调试模式），那么要在运行服务器之前导出 `FLASK_ENV` 环境变量并把其设置为 `development`:

```
$ export FLASK_ENV=development
$ flask run
```

（在 Windows 下需要使用 `set` 来代替 `export` 。）

------

`FLASK_ENV` 变量用来告诉Flask当前应用所运行的环境，有两个值，分别是 “production” 和 “development”，默认缺省值是“production”。

Flask自身和第三方扩展插件可能会基于此变量值改变自己的行为。

如果设置为：“development”，那么可实现：

1、激活调试器。 2、激活自动重载。 3、打开 Flask 应用的调试模式。

只要项目中代码有发生变化，程序就会自动重启。 在开发调试过程中很有用，如果是production，每次还要手动重启。

还可以通过导出 `FLASK_DEBUG=1` 来单独控制调试模式的开关。

> Attention
>
> 虽然交互调试器不能在分布环境下工作（这使得它基本不可能用于生产环境），但是 它允许执行任意代码，这样会成为一个重大安全隐患。因此， **绝对不能在生产环境 中使用调试器** 。

开启调试模式与不开启调试在网页上看到的区别是这样的：

- 未开启调试模式：

![未开启调试模式](.\images\未开启调试模式.png)

- 开启调试模式：

  ![开启调试模式](.\images\开启调试模式.png)

在正式环境我们是严格要求关闭调试模式的。





   





