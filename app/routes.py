#!/usr/bin/python
# coding: utf-8
# -*- coding: utf-8 -*-

#从app模块中即从__init__.py中导入创建的app应用
from app import app,db
from flask import render_template,flash,redirect,url_for,request

from werkzeug.urls import url_parse

from app.forms import LoginForm,RegistrationForm

from flask_login import current_user, login_user,logout_user,login_required
from app.models import User



#建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
@app.route('/index')

#这样，必须登录后才能访问首页了,否则会自动跳转至登录页
#@login_required


def index():
    #user={'username':'dairen'}

    posts = [
        {
            'author': {'username': '张三'},
            'body': '你好～1'

        },
        {
            'author': {'username': '李四'},
            'body': '你好～2'
        }
    ]
    return render_template('index.html',title='我的博客',posts=posts)

'''
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    #验证表格中的数据格式是否正确
    if form.validate_on_submit():
        #闪现的信息会出现在页面，当然在页面上要设置
        flash('用户登录的名户名是:{} , 是否记住我:{}'.format(form.username.data,form.remember_me.data))
        #重定向至首页
        return redirect(url_for('index'))
    #首次登录/数据格式错误都会是在登录界面
    return render_template('login.html',title='登录',form=form)
'''

@app.route('/login',methods=['GET','POST'])
def login():
    #判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        flash('请先退出当前账号！')
        return redirect(url_for('index'))
    form = LoginForm()

    #对表格数据进行验证
    if form.validate_on_submit():
        #根据表格里的数据进行查询，如果查询到数据返回User对象，否则返回None
        user = User.query.filter_by(username=form.username.data).first()
        #判断用户不存在或者密码不正确
        if user is None or not user.check_password(form.password.data):
            #如果用户不存在或者密码不正确就会闪现这条信息
            flash('无效的用户名或密码')
            #然后重定向到登录页面
            return redirect(url_for('login'))
        #这是一个非常方便的方法，当用户名和密码都正确时来解决记住用户是否记住登录状态的问题
        login_user(user,remember=form.remember_me.data)

        #此时的next_page记录的是跳转至登录页面是的地址
        next_page = request.args.get('next')
        # 如果next_page记录的地址不存在那么就返回首页
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        # 综上，登录后要么重定向至跳转前的页面，要么跳转至首页
        return redirect(url_for('index'))

    #既没有提交数据，也没有认证过的用户，直接返回登录页面
    return render_template('login.html',title='登录',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET', 'POST'])
def register():
    # 判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        flash('请先退出当前账号，再进行注册!')
        return redirect(url_for('index'))
    form = RegistrationForm()

    #如果提交了注册的表单，则进行处理
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('恭喜你!已成为我们网站的新用户!')
        return redirect(url_for('login'))

    #如果没有提交注册表单，则定向到注册页面
    return render_template('register.html', title='注册', form=form)