#!/usr/bin/env python
import os
from app import create_app, db
from flask.ext.script import Manager, Shell

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()