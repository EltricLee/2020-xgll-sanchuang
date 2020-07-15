from .base import db

def init_app(app):
	db.init_app(app)
	#下面这句，可有可无
	#db.create_all(app=app)
