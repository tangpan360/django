# Django学习路线图与进度追踪

## Django项目结构图

```
mysite/                  # 项目根目录
│
├── manage.py            # Django命令行工具
│
├── mysite/              # 项目主包
│   ├── __init__.py      # 空文件，标识Python包
│   ├── settings.py      # 项目配置文件
│   ├── urls.py          # 项目URL配置
│   ├── asgi.py          # ASGI兼容的Web服务器入口
│   └── wsgi.py          # WSGI兼容的Web服务器入口
│
├── blog/                # 应用目录
│   ├── __init__.py      # 空文件，标识Python包
│   ├── admin.py         # Django管理后台配置
│   ├── apps.py          # 应用配置
│   ├── migrations/      # 数据库迁移文件目录
│   │   └── __init__.py  # 空文件，标识Python包
│   ├── models.py        # 数据模型定义
│   ├── tests.py         # 测试代码
│   ├── urls.py          # 应用URL配置
│   └── views.py         # 视图函数/类
│
├── templates/           # 全局模板目录
│   ├── base.html        # 基础模板
│   └── blog/            # 应用专用模板
│       ├── index.html   # 博客首页模板
│       └── detail.html  # 博客详情页模板
│
└── static/              # 静态文件目录
    ├── css/             # CSS文件
    ├── js/              # JavaScript文件
    └── images/          # 图片文件
```

这是一份Django全面学习计划，按照循序渐进的方式组织，从基础概念到高级特性，最终构建一个完整的博客系统。每完成一项任务，可以在方框中打勾(✓)标记进度。

## 第一阶段：环境准备与基础知识 (1周)

### 开发环境配置
- [✓] 安装Python并创建虚拟环境
- [✓] 安装 Django 最新版本
- [✓] 创建第一个Django项目 (`django-admin startproject mysite`)
- [✓] 运行开发服务器并访问 (`python manage.py runserver`)

### Django基础概念
- [✓] 学习MTV架构模式(Model-Template-View)
- [✓] 了解Django项目结构与文件作用
- [✓] 掌握settings.py配置文件的主要设置项
- [✓] 理解urls.py路由系统的工作原理

### 实践任务
- [✓] 创建第一个应用 (`python manage.py startapp blog`)
- [✓] 在settings.py中注册应用
- [✓] 创建第一个视图函数并配置URL
- [✓] 运行并测试应用

## 第二阶段：模型与数据库 (2周)

### 模型定义
- [ ] 了解Django ORM基础概念
- [ ] 学习常用字段类型(CharField, TextField, DateTimeField等)
- [ ] 掌握字段选项(max_length, null, blank, default等)
- [ ] 创建模型方法(包括`__str__`方法)

### 数据库操作
- [ ] 执行数据库迁移命令(makemigrations, migrate)
- [ ] 学习基本查询操作(all, get, filter, exclude)
- [ ] 掌握高级查询(Q对象, F对象, 聚合函数)
- [ ] 理解模型关系(ForeignKey, ManyToManyField, OneToOneField)

### Django Admin
- [ ] 配置Admin站点
- [ ] 注册模型到Admin
- [ ] 自定义Admin界面(ModelAdmin类)
- [ ] 添加搜索和过滤功能

### 实践任务
- [ ] 设计博客数据模型(用户、文章、分类、评论)
- [ ] 创建模型间的关系
- [ ] 注册模型到Admin后台
- [ ] 通过Admin添加一些测试数据

## 第三阶段：视图与URL (1-2周)

### 函数视图
- [ ] 编写基本视图函数
- [ ] 处理请求参数(GET, POST)
- [ ] 使用快捷函数(render, redirect, get_object_or_404)
- [ ] 实现请求处理逻辑

### 类视图
- [ ] 学习基于类的视图(Class-Based Views)
- [ ] 使用通用视图(ListView, DetailView等)
- [ ] 理解视图混入(Mixins)
- [ ] 自定义类视图方法(get_queryset, get_context_data等)

### URL配置
- [ ] 配置应用级URL模式
- [ ] 使用路径转换器(path converters)
- [ ] 命名URL模式和命名空间
- [ ] 包含其他URL配置(include)

### 实践任务
- [ ] 实现文章列表视图
- [ ] 实现文章详情视图
- [ ] 创建文章创建、编辑、删除视图
- [ ] 配置完整的URL结构

## 第四阶段：模板与表单 (2周)

### 模板系统
- [ ] 创建基本模板
- [ ] 使用模板变量和过滤器
- [ ] 掌握模板标签(if, for, url等)
- [ ] 学习自定义模板过滤器和标签

### 模板继承
- [ ] 创建基础模板(base.html)
- [ ] 定义块(block)和继承
- [ ] 使用include标签复用模板
- [ ] 实现导航和页面布局

### 表单处理
- [ ] 创建表单类(Form和ModelForm)
- [ ] 在视图中处理表单提交
- [ ] 表单验证和错误处理
- [ ] 自定义表单字段和小部件(widgets)

### 实践任务
- [ ] 创建博客前端页面(首页、列表页、详情页)
- [ ] 实现文章创建和编辑表单
- [ ] 添加评论表单
- [ ] 实现表单验证和错误提示

## 第五阶段：用户认证与权限 (1周)

### 用户系统
- [ ] 使用Django内置用户模型
- [ ] 实现用户注册功能
- [ ] 创建登录和退出视图
- [ ] 添加密码重置功能

### 权限控制
- [ ] 使用装饰器限制访问(login_required, permission_required)
- [ ] 在类视图中使用Mixin控制访问
- [ ] 实现对象级权限
- [ ] 自定义用户权限

### 实践任务
- [ ] 创建用户注册和登录页面
- [ ] 实现用户个人资料页面
- [ ] 添加权限控制(只有作者可以编辑文章)
- [ ] 实现管理员特殊权限

## 第六阶段：REST API开发 (2周)

### Django REST framework
- [ ] 安装和配置DRF
- [ ] 了解API基础概念(REST, HTTP方法)
- [ ] 学习请求/响应处理
- [ ] 掌握内容协商(JSON, XML)

### 序列化器
- [ ] 创建基本序列化器
- [ ] 使用ModelSerializer
- [ ] 嵌套序列化和关系处理
- [ ] 自定义字段和验证

### API视图
- [ ] 编写基于函数的API视图
- [ ] 使用基于类的API视图
- [ ] 实现ViewSets和Routers
- [ ] 添加分页、过滤和排序

### 实践任务
- [ ] 为博客文章创建API端点
- [ ] 实现用户认证(Token或JWT)
- [ ] 添加权限控制
- [ ] 编写API文档

## 第七阶段：高级特性 (2周)

### 中间件
- [ ] 了解中间件工作原理
- [ ] 创建自定义中间件
- [ ] 使用内置中间件
- [ ] 中间件执行顺序

### 信号系统
- [ ] 学习内置信号(pre_save, post_save等)
- [ ] 连接信号接收器
- [ ] 创建自定义信号
- [ ] 使用信号实现解耦功能

### 缓存系统
- [ ] 配置缓存后端
- [ ] 使用视图缓存装饰器
- [ ] 实现模板片段缓存
- [ ] 低级缓存API使用

### 实践任务
- [ ] 添加文章搜索功能
- [ ] 实现标签系统
- [ ] 创建文章草稿功能
- [ ] 优化性能(缓存热门文章)

## 第八阶段：测试与部署 (2周)

### 单元测试
- [ ] 编写模型测试
- [ ] 创建视图测试
- [ ] 表单测试
- [ ] 使用测试客户端

### 静态文件处理
- [ ] 配置静态文件目录
- [ ] 使用collectstatic命令
- [ ] 添加CSS和JavaScript
- [ ] 处理用户上传文件

### 部署准备
- [ ] 配置生产环境设置
- [ ] 设置环境变量
- [ ] 配置数据库连接
- [ ] 安全设置(HTTPS, CSRF等)

### 实践任务
- [ ] 编写完整测试套件
- [ ] 准备部署配置
- [ ] 部署到生产服务器
- [ ] 设置持续集成/部署

## 综合实践项目：构建完整的内容管理系统

### 功能开发清单
- [ ] 用户认证与权限管理
- [ ] 内容创建、编辑、发布
- [ ] 评论与互动系统
- [ ] 文件上传与管理
- [ ] 搜索与过滤功能
- [ ] RESTful API
- [ ] 后台管理界面定制