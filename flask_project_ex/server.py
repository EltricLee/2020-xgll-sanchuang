#导入flask核心
from flask import Flask
#实例化一个app

#Flask
#字符串用来Flask对象标识，通常用__name__
app = Flask(__name__)

#加载配置
app.config.from_object('config.settings')
app.config.from_object('config.secure')

#注册路由/index/
#支持正则
#app.router(路由规则)
@app.route("/index/",methods=["POST"],endpoint="index001")
def index():
	return "this is index"

def index2():
	return "this is index2"
app.add_url_rule('/index2/',view_func=index2)

#运行app
#debug=True =>热启动 =》代码做了修改，自动重启
app.run(
	host=app.config['HOST'],
	port=app.config['PORT'],
	debug=app.config['DEBUG'],
)

