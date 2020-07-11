#加载配置
#注册路由/index/
#支持正则
#app.router(路由规则)
from app import create_app
app = create_app()

@app.route("/index/",methods=["POST"],endpoint="index001")
def index():
	return "this is index"

def index2():
	return "this is index2"
app.add_url_rule('/index2/',view_func=index2)