#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from . import login_manager





class User(db.Model):
    '''创建用户表'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(64),unique=True,index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    '''创建角色表'''
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name