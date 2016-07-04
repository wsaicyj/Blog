#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

#保存程序的路由

from datetime import datetime
from flask import render_template,session,redirect,url_for,abort,flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from flask_login import login_required,current_user
from .forms import EditProfileForm

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

@main.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    '''资料编辑路由'''
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user',username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',form=form)