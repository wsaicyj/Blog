#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin,AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app



class User(UserMixin,db.Model):
    '''创建用户表'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean,default=False)
    
    #定义默认的用户角色
    def __init__(self,**kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is not None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(perssion=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def __repr__(self):
        return '<User %r>' % self.username

    #检查用户是否有指定的权限
    def can(self,permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    #判断用户权限是否为管理员
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #生成包含用户id的安全令牌
    def generate_confirmation_token(self,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})

    #确认用户账户
    def confirm(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    '''
    创建角色表
    匿名   0b00000000（0x00） 未登录的用户。在程序中只有阅读权限
    用户   0b00000111（0x07） 具有发布文章、发表评论和关注其他用户的权限。这是新用户的默认角色
    协管员 0b00001111（0x0f） 增加审查不当评论的权限
    管理员 0b11111111（0xff） 具有所有权限，包括修改其他用户所属角色的权限
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    default = db.Column(db.Boolean,default=False,index=True)
    permission = db.Column(db.Integer)
    users = db.relationship('User',backref='role',lazy='dynamic')


    @staticmethod
    def insert_roles():
        roles = {
            'User':(Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES,True),
            'Moderator':(Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS,False),
            'Administrator':(0xff,False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permission = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class Permission:
    '''权限常量'''
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class AnonymousUser(AnonymousUserMixin):
    def can(self,permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser