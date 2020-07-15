#加载配置
#注册路由/index/
#支持正则
#app.router(路由规则)
from flask import Blueprint
view2_bp = Blueprint('view2',__name__,url_prefix='/view2/')

@view2_bp.route("index/",methods=["POST"],endpoint="index001")
def index():
	return "this is index"

def index2():
	return "this is index2"
view2_bp.add_url_rule('index2/',view_func=index2)