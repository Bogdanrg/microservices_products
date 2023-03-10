from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_script._compat import text_type


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
