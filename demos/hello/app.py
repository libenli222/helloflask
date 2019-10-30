# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask

app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# 设置默认值方法一
# dynamic route, URL variable default
@app.route('/greet/<name>')
@app.route('/greet', defaults={'name': 'Programmer'})
# @app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# 设置默认值方法二
@app.route('/groot')
@app.route('/groot/<name>')
def groot(name='grlibenli'):
    return "<h1>hello,%s!<h1>" % name


# custom flask cli command
# 创建自定义命令,默认函数名hello，
# 可以在装饰器中修改nohello
@app.cli.command('nohello')
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')

# 不通过黑屏终端执行程序or设置 edit configurations
# if __name__ == "__main__":
#     app.run()
