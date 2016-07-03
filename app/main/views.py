#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

#保存程序的路由

from datetime import datetime
from flask import render_template,session,redirect,url_for,abort
from . import main
from .forms import NameForm
from .. import db
from ..models import User

'''
@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False),current_time=datetime.utcnow())
'''

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    '''资料页面的路由'''
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html',user=user)