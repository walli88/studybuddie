#!/usr/bin/env python
import os
from angular_flask import create_app, db
from flask.ext.script import Manager, Shell
# from flask.ext.migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)

# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()