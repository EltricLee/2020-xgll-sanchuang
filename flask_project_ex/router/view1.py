#加载配置
#注册路由/index/
#支持正则
#app.router(路由规则)
from flask import Blueprint,render_template
from models.example1 import Article,Banner,News

view1_bp = Blueprint('view1',__name__,url_prefix='')


@view1_bp.route("index/",methods=["POST","GET"],endpoint="index001")
def index():
	lead_news = {
			'title':"塞尔维亚各界期待习近平主席到访",
			'content':"国家主席习近平将对塞尔维亚进行国事访问。塞尔维亚各界热切期待习近平主席的到访。",
	}
	articles = Article.query.order_by(Article.count.desc()).all()
	banners = Banner.query.all()
	news = News.query.all()
	# print(articles[0],type(articles[0]))
	# print(articles)
	context = {
		"lead_news":lead_news,
		"articles":articles,
		"banners":banners,
		"news":news,
	}
	return render_template('index.html',**context)

def index2():
	return "this is index2"
view1_bp.add_url_rule('index2/',view_func=index2)
