"""
该类设置路由
"""

from appdir import app, config
from appdir.forms import AnswerForm
from appdir.models import *
from flask import render_template, redirect, url_for, flash, request, jsonify

from appdir.utils.article_dataset import dic_article
from appdir.utils.util import validate_register, validate_login, addQuestion, get_all_questions, getAnswerById, \
    solveDailyReminder, solveObjectivesForm, solveReportsForm, solveDailyDataForm


# 根路由
@app.route('/', methods=['GET', 'POST'])
def root():
    return index()


# 首页
@app.route('/index', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')


# 首页
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


# 注册
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


# 消息页
@app.route('/info', methods=['GET', 'POST'])
def info():  # put application's code here
    return render_template('info.html')


# ——————————————————————————————————————————————————————————————————
# 个人中心
@app.route('/personCenter', methods=['GET', 'POST'])
def personCenter():  # put application's code here
    return render_template('personCenter.html')


# dailyReminderForm.html
@app.route('/dailyReminderForm', methods=['GET', 'POST'])
def dailyReminderForm():  # put application's code here
    if request.method == 'POST':
        dailyReminder = request.form.get('dailyReminder')
        solveDailyReminder(dailyReminder)
        return render_template('personCenterForm/dailyReminderForm.html', dailyReminder=dailyReminder)
    return render_template('personCenterForm/dailyReminderForm.html')


@app.route('/objectivesForm', methods=['GET', 'POST'])
def objectivesForm():  # put application's code here
    if request.method == 'POST':
        medicalAdvice = request.form.get('medicalAdvice')
        managementObjectives = request.form.get('managementObjectives')
        solveObjectivesForm(medicalAdvice, managementObjectives)
        return render_template('personCenterForm/objectivesForm.html', medicalAdvice=medicalAdvice,
                               managementObjectives=managementObjectives)
    return render_template('personCenterForm/objectivesForm.html')


# reportsForm.html
@app.route('/reportsForm', methods=['GET', 'POST'])
def reportsForm():  # put application's code here
    if request.method == 'POST':
        hbA1c = request.form.get('hbA1c')
        insulin = request.form.get('insulin')
        ogtt = request.form.get('ogtt')
        insulinTest = request.form.get('insulinTest')
        cPeptide = request.form.get('cPeptide')
        diabetesAb = request.form.get('diabetesAb')
        bloodPressure = request.form.get('bloodPressure')
        bloodLipid = request.form.get('bloodLipid')
        solveReportsForm(
            hbA1c=hbA1c,
            insulin=insulin,
            ogtt=ogtt,
            insulinTest=insulinTest,
            cPeptide=cPeptide,
            diabetesAb=diabetesAb,
            bloodPressure=bloodPressure,
            bloodLipid=bloodLipid
        )
        return render_template('personCenterForm/reportsForm.html',
                               hbA1c=hbA1c,
                               insulin=insulin,
                               ogtt=ogtt,
                               insulinTest=insulinTest,
                               cPeptide=cPeptide,
                               diabetesAb=diabetesAb,
                               bloodPressure=bloodPressure,
                               bloodLipid=bloodLipid)
    return render_template('personCenterForm/reportsForm.html')


@app.route('/dailyDataForm', methods=['GET', 'POST'])
def dailyDataForm():  # put application's code here
    if request.method == 'POST':
        blood_glucose = request.form.get('blood_glucose')
        diet_composition = request.form.get('diet_composition')
        exercise_amount = request.form.get('exercise_amount')
        solveDailyDataForm(blood_glucose=blood_glucose,
                           diet_composition=diet_composition,
                           exercise_amount=exercise_amount)
        return render_template('personCenterForm/dailyDataForm.html',
                               blood_glucose=blood_glucose,
                               diet_composition=diet_composition,
                               exercise_amount=exercise_amount)
    return render_template('personCenterForm/dailyDataForm.html')


# ——————————————————————————————————————————————————————————————————————

# 关于我们
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


# 访问论坛
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    return render_template('forum.html', questions=get_all_questions())


# 问题详情页
@app.route('/question<question_id>', methods=['GET', 'POST'])
def question(question_id):
    current_question = Question.query.filter(Question.id == question_id).first()
    answers = getAnswerById(question_id)
    answer_form = AnswerForm()
    return render_template('question.html',
                           question=current_question, answers=answers,
                           answer_form=answer_form)


# ————————————————————————————————————————————————————————————
# 以下为文章的路由地址

@app.route('/article<id>', methods=['GET', 'POST'])
def article(id):
    link = dic_article[int(id)]
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
