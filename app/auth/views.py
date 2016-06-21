#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from flask import render_template
from . import auth



@auth.route('/login')
def login():
    return render_template('auth/login.html')

