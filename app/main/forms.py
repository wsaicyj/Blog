#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
    '''
    表格类
    '''

    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')
