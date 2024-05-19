# TowerTiltDetection

APRU竞赛的WEB展示项目

## 启动项目

1. 安装[requirements.txt](requirements.txt)的依赖
2. 在命令行输入

- 初始化数据库

```shell
flask initdb --drop
```

- 导入文章数据

```shell
flask addArticle
```

- 初始化论坛

```shell
flask initForum
```

3. 启动项目`app.py`即可

```shell
python app.py
```

4. 如果你需要打包项目成exe文件，可以使用下面的命令：

```shell
pyinstaller APRUapp.spec
```

（注意：默认的exe文件存放在`dist`文件夹下面）

## 完成模块

### 项目信息

- 完成项目文章展示，使用`pandoc`转化
- 完成项目文章连接跳转

### 论坛 & 咨询

- 完成咨询表单，提交完毕可以在论坛看见
- 论坛可以查看答案
- 论坛暂无网页回答，只能后端录入回答

### 个人中心

- 登录
- 注册
- 个人数据查看

