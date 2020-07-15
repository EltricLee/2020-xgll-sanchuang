from .view1 import view1_bp
from .view2 import view2_bp

def init_app(app):
	# app核心对象
	app.register_blueprint(view1_bp)
	app.register_blueprint(view2_bp)


