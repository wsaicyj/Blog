#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'


from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s!</h1>' % user_agent
    #return '<h1>hello,Flask</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)