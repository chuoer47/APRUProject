"""
该类设置路由
"""

from appdir import app
from appdir.forms import RegisterForm, LoginForm
from appdir.models import *
from flask import render_template, redirect, url_for, flash, request
from appdir.utils.util import validate_register, validate_login, addQuestion


@app.route('/', methods=['GET', 'POST'])
def root():
    return index()


@app.route('/index', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return validate_login(login_form)
    return render_template('login.html', form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        return validate_register(register_form)
    return render_template('register.html', form=register_form)


@app.route('/info', methods=['GET', 'POST'])
def info():  # put application's code here
    return render_template('info.html')


@app.route('/relateUs', methods=['GET', 'POST'])
def relateUs():  # put application's code here
    return render_template('relateUs.html')


# 添加论坛问题
@app.route('/ask', methods=['GET', 'POST'])
def ask():  # put application's code here
    if request.method == 'POST':
        title = request.form.get('title')
        question = request.form.get('question')
        addQuestion(title, question)  # 数据库添加论坛问题
        return render_template('ask.html', title=title, question=question, message="success")
    else:
        return render_template('ask.html')


# 以下为尚未完成的部分
@app.route('/test', methods=['GET', 'POST'])
def test():  # put application's code here
    return redirect(url_for('ask', message="success"))


@app.route('/user', methods=['GET', 'POST'])
def user():  # put application's code here
    user = User.query.get(1)
    return render_template('test.html', userName=user.username, userPass=user.password)
