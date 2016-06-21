#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
创建认证蓝本
'''
__author__ = 'Aaron_chan'

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views