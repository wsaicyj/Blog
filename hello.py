#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'


from flask import Flask,render_template,session,redirect,url_for,flash
from flask import request
from flask import make_response
from flask import abort
#from flask.ext.script import Manager
from flask_script import Manager
#from flask.ext.bookstrap import Bootstrap
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SECRET_KEY'] =  'hard to guess string'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite') #配置数据库
app.config['SQLCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
#manager = Manager(app)

bootstarp = Bootstrap(app)

moment = Moment(app)

@app.route('/',methods=['GET','POST'])
def index():
    #name = None
    form = NameForm()
    if form.validate_on_submit():
        #form.name.data = ''
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

@app.route('/page_not_found')
def page_not_found(e):
    return render_template('404.html')

@app.route('/500')
def internal_server_error(e):
    return render_template('500.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

'''
@app.route('/')
def index():
    #user_agent = request.headers.get('User-Agent')
    #return '<h1>Your browser is %s!</h1>' % user_agent
    #return '<h1>hello,Flask</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>hello,%s!</h1>' % name
    return render_template('user.html',name=name)

@app.route('/response')
def cook():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

@app.route('/user1/<id>')
def get_user(id):
    #user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s!</h1>' % user.name
'''


class NameForm(Form):
    '''
    表格类
    '''

    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')


class Role(db.Model):
    '''创建角色表'''
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    '''创建用户表'''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    app.run(debug=True)
    #manager.run()