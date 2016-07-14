#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

#存储配置

import os

#获取当前项目路径
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <wsaicyj@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''开发环境'''
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'wsaicyj@163.com'
    MAIL_PASSWORD = 'cyj232238230'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASK_MAIL_SENDER = 'Flask Admin <wsaicyj@163.com>'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/blog'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/blog'
    FLASKY_POSTS_PER_PAGE = 10


class TestingConfig(Config):
    '''测试环境'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    '''生产环境'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}