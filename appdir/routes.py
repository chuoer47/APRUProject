"""
该类设置路由
"""

from appdir import app, config
from appdir.forms import AnswerForm
from appdir.models import *
from flask import render_template, redirect, url_for, flash, request, jsonify

from appdir.utils.dict_article import dic_article
from appdir.utils.util import validate_register, validate_login, addQuestion, get_all_questions, getAnswerById


@app.route('/', methods=['GET', 'POST'])
def root():
    return index()


@app.route('/index', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        validate_login(username, password)
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        validate_register(username, password, repassword)
        return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/info', methods=['GET', 'POST'])
def info():  # put application's code here
    return render_template('info.html')


@app.route('/personCenter', methods=['GET', 'POST'])
def personCenter():  # put application's code here
    return render_template('personCenter.html')


@app.route('/relateUs', methods=['GET', 'POST'])
def relateUs():  # put application's code here
    return render_template('relateUs.html')


# 添加论坛问题
@app.route('/consult', methods=['GET', 'POST'])
def consult():  # put application's code here
    if request.method == 'POST':
        title = request.form.get('title')
        question = request.form.get('question')
        addQuestion(title, question)  # 数据库添加论坛问题
        return render_template('consult.html', title=title, question=question, message="success")
    else:
        return render_template('consult.html')


# 获取json格式的所有问题
@app.route('/get_all_questions', methods=['GET', 'POST'])
def getAllQuestions():  # put application's code here
    return jsonify(get_all_questions())


# 访问论坛
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    return render_template('forum.html', questions=get_all_questions())


@app.route('/question<question_id>', methods=['GET', 'POST'])
def question(question_id):
    current_question = Question.query.filter(Question.id == question_id).first()
    answers = getAnswerById(question_id)
    answer_form = AnswerForm()
    return render_template('question.html',
                           question=current_question, answers=answers,
                           answer_form=answer_form)


# ————————————————————————————————————————————————————————————
# 以下为文章的路由地址，由于我不会统一开发，只能这样子


@app.route('/article<id>', methods=['GET', 'POST'])
def article(id):
    link = dic_article[id]
    return render_template(link)


# ——————————————————————————————————————————————————————————————————

# 以下为尚未完成的部分
@app.route('/test', methods=['GET', 'POST'])
def test():  # put application's code here
    return redirect(url_for('ask', message="success"))


@app.route('/user', methods=['GET', 'POST'])
def user():  # put application's code here
    user = User.query.get(1)
    return render_template('test.html', userName=user.username, userPass=user.password)
