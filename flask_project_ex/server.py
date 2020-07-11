#导入flask核心
from flask import Flask
#实例化一个app

#Flask
#字符串用来Flask对象标识，通常用__name__
app = Flask(__name__)

#注册路由/index/
#支持正则
#app.router(路由规则)
@app.route("/index/")
def index():
	return "this is index"

def index2():
	return "this is index2"
app.add_url_rule('/index2/',view_func=index2)

#运行app

app.run()

