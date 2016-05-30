#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'


from flask import Flask
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s!</h1>' % user_agent
    #return '<h1>hello,Flask</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>' % name

@app.route('/response')
def cook():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

@app.route('/user1/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s!</h1>' % user.name


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()