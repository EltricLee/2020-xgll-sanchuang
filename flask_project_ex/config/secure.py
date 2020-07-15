import  os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

PassWord = "123456"

DEBUG = True
ENV = "development"

#使用sqlite数据库

SQLALCHEMY_DATABASE_URI = 'sqlite:///' +  os.path.join(basedir, 'data.sqlite')