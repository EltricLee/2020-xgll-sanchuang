from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app
from models import db

app = create_app()
#
manager = Manager(app)

##由于此处，使用的是sqlite数据库，sqlite数据库不支持列删除操作
#migrate = Migrate(app,db)

with app.app_context():
	migrate = Migrate()
	if db.engine.url.drivername == 'sqlite':
		migrate.init_app(app,db,render_as_batch=True)
	else:
		migrate.init_app(app,db)

manager.add_command('db',MigrateCommand)



if __name__ == "__main__":
	manager.run()
