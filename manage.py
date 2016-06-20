#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

#用于启动程序及其他的程序任务

import os
from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command('shell',Shell(make_context=make_shell_context()))
manager.add_command('db',)


if __name__ == '__main__':
    manager.run()