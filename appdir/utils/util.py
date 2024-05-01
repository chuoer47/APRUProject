from flask import flash, redirect, url_for, session
from werkzeug.security import check_password_hash

from appdir import app, db
from appdir.models import User, Question


def validate_register(form):
    if form.password.data != form.repassword.data:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('register'))
    if User.query.filter(User.username == form.username.data).first():
        flash('The username has been used!', 'error')
        return redirect(url_for('register'))
    password = form.password.data
    user = User(username=form.username.data, password=password)
    db.session.add(user)
    db.session.commit()
    flash('User registered with username: {}'.format(form.username.data), 'success')
    return redirect(url_for('index'))


def validate_login(form):
    user_in_db = User.query.filter(User.username == form.username.data).first()
    if not user_in_db:
        flash('No user found with username: {}'.format(form.username.data), 'error')
        return redirect(url_for('login'))
    if user_in_db.password == form.password.data:
        flash('Login successfully!', 'success')
        session["USERNAME"] = user_in_db.username
        session["USERID"] = user_in_db.id
        return redirect(url_for('root'))
    flash('Incorrect Password', 'error')
    return redirect(url_for('login'))


# 添加问题到数据库
def addQuestion(title, question):
    question = Question(title=title, question=question)
    db.session.add(question)
    db.session.commit()
    flash("success question with title:{}".format(title), 'success')
    return
