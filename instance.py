#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'


from hello import app
from flask import current_app

#print(current_app.name)
app_cntx = app.app_context()
app_cntx.push()
print(current_app.name)
print(app.url_map)