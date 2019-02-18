#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

#导入配置文件
from config import Config

#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)

#添加配置信息
app.config.from_object(Config)

#登录
login=LoginManager(app)

#限制一些页面 登录用户才能看到
login.login_view = 'login'

#建立数据库关系
db = SQLAlchemy(app)
#绑定app和数据库，以便进行操作
migrate = Migrate(app,db)


from app import routes, models
