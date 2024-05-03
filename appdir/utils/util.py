from datetime import datetime

from flask import flash, redirect, url_for, session, jsonify

from appdir import app, db
from appdir.models import User, Question, Answer


def validate_register(username, password, repassword):
    if password != repassword:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('register'))
    if User.query.filter(User.username == username).first():
        flash('The username has been used!', 'error')
        return redirect(url_for('register'))
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    flash('User registered with username: {}'.format(username), 'success')
    return redirect(url_for('index'))


def validate_login(username, password):
    user_in_db = User.query.filter(User.username == username).first()
    if not user_in_db:
        flash('No user found with username: {}'.format(username), 'error')
        return redirect(url_for('login'))
    if user_in_db.password == password:
        flash('Login successfully!', 'success')
        session["USERNAME"] = user_in_db.username
        session["USERID"] = user_in_db.id
        return redirect(url_for('root'))
    flash('Incorrect Password', 'error')
    return redirect(url_for('login'))


# 添加问题到数据库
def addQuestion(title, question):
    now_time = datetime.now()
    question = Question(title=title, question=question, datetime=now_time)
    db.session.add(question)
    db.session.commit()
    flash("success question with title:{}".format(title), 'success')
    return


def get_all_questions():
    questions = Question.query.all()

    question_data = []
    for question in questions:
        question_data.append({
            'id': question.id,
            'title': question.title,
            'question': question.question,
            'datetime': question.datetime,
            'user_id': question.user_id
        })
    return question_data


def getAnswerById(questionId):
    answers = Answer.query.filter(Answer.question_id == questionId)

    answer_data = []
    for answer in answers:
        answer_data.append({
            'id': answer.id,
            'content': answer.content,
            'user_id': answer.user_id,
            'question_id': answer.question_id
        })
    return answer_data
