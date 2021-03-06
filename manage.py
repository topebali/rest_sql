from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import app
import models

manager = Manager(app)

db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app, db)



def make_shell_context():
    """
    Ensures returned values are accessible in the interactive shell
    without importing them.
    :return: a dictionary of values to be imported
    """
    return dict(app=app, db=data.db)

# Ensures the values in the first parameters can be passed when running
# this file, activating the second parameters.
# Example: python manage.py shell
# Would activate the second parameter Shell.


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()