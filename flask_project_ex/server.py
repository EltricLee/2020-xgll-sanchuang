from app import create_app
from router.view import app
#实例化一个app

#运行app
#debug=True =>热启动 =》代码做了修改，自动重启

if __name__ == "__main__":
	app.run(
		host=app.config['HOST'],
		port=app.config['PORT'],
		debug=app.config['DEBUG'],
	)

