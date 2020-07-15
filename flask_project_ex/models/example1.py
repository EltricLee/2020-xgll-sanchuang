from sqlalchemy import Column,Integer,String
'''
文章表：文章标题/点击量
'''
from .base import db
#定义数据模型(一个类就是一张表/一个属性就是一个字段)
class Article(db.Model):
	id = Column(Integer,primary_key=True,autoincrement=True)
	title = Column(String(128),nullable=True)
	count = Column(Integer,nullable=True)
	count2 = Column(Integer, nullable=True)

#代码 -》数据模型 ——》数据库

class Banner(db.Model):
	id = Column(Integer,primary_key=True,autoincrement=True)
	title = Column(String(128),nullable=True)
	cover_url = Column(String(255),nullable=True)

class News(db.Model):
	id = Column(Integer,primary_key=True,autoincrement=True)
	title = Column(String(128),nullable=False)
	sub_title = Column(String(128),nullable=True)
	content = Column(String(255),nullable=True)

