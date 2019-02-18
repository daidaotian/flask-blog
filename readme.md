#python知识点
###数据库

建表：
flask db migrate -m 'posts_table'
flask db upgrade

查询：
posts = Post.query.all()
>>> for p in posts:
...     print(p.id,p.author.username,p.body)

User.query.order_by(User.username.desc()).all()

删除：
users = User.query.all()
>>> for u in users:
...     db.session.delete(u)


密码加密：
from werkzeug.security import generate_password_hash
>>> hash = generate_password_hash('mima')
>>> hash
'pbkdf2:sha256:50000$S9FPhxbX$4f164ff06b409769e44556bcd9d8f906ca82998e433410f85898245e40ecd4d3'

加密验证：
>>> from werkzeug.security import check_password_hash
>>> check_password_hash(hash,'haha')
False
>>> check_password_hash(hash,'mima')
True

###flask-login
flask中有很多写的非常不错的插件，像flask-migrate就很不错，这里介绍一个flask-login，当然你肯定可以自己从写一个，但是有别人造好的轮子为什么先不体验一下试试呢？

###__init__.py
Python包的标识符。python包实际上就是一个文件夹，__init__.py的作用就是把这个文件夹变成一个可识别的python包。如果没有__init__.py文件，则该文件夹只是一个普通的目录

Python中的包和模块有两种导入方式：精确导入和模糊导入：

精确导入：

from Root.Pack1 import Pack1Class

import Root.Pack1.Pack1Class
模糊导入：

from Root.Pack1 import *
模糊导入中的*中的模块是由__all__来定义的，__init__.py的另外一个作用就是定义package中的__all__，用来模糊导入，如__init__.py：

    __all__ = ["Pack1Class","Pack1Class1"]

### python新式类 经典类
新式类是指继承object的类，修复了经典类中多继承出现的bug
    class A(object):
      ...........
经典类是指没有继承object的类
    class A:

#flask 知识点
url_for 这是根据视图函数名返回url


#html知识点
{{ }} 意味着变量，可以接受数据的地方
<hr /> 标签在 HTML 页面中创建水平线。

<!--这是一段注释。注释不会在浏览器中显示。-->

<br /> 标签，换行

HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息，属性总是在 HTML 元素的开始标签中规定
<a> 标签中必须提供 href 属性或 name 属性
href 属性的值可以是任何有效文档的相对或绝对 URL，包括片段标识符和 JavaScript 代码段

<div> 标签可以把文档分割为独立的、不同的部分。它可以用作严格的组织工具，并且不使用任何格式与其关联。
如果用 id 或 class 来标记 <div>，那么该标签的作用会变得更加有效

{% block content %} {% endblock %}这一对标签，因此其他页面只需要继承这个页面，然后写上相同的标签，在标签内写上内容，就可以完整的在页面上显示所有内容

<ul> </ul>无序 HTML 列表
<li> 标签定义列表项目。<li> 标签可用在有序列表 (<ol>) 和无序列表 (<ul>) 中
