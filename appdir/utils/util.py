from datetime import datetime

from flask import flash, redirect, url_for, session

from appdir import db
from appdir.models import User, Question, Answer, DailyReminder, Objectives, HospitalExaminationReports, DailyData, \
    Article


# ——————————————————————————————————————
# 下面为注册登录所需方法
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


# ——————————————————————————————


# ——————————————————————————————
# 添加问题到数据库
def addQuestion(title, question):
    if not title and not question:
        flash("Please fill in all the required fields", 'error')
        return redirect(url_for('consult'))
    now_time = datetime.now()
    question = Question(title=title, question=question, datetime=now_time)
    db.session.add(question)
    db.session.commit()
    flash("success question with title:{}".format(title), 'success')
    return


# ——————————————————————————————


# ————————————————————————————————————
# 下面为论坛的开发模块需要的方法
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


# 获得所有文章
def get_all_articles():
    datas = Article.query.all()
    resultList = []
    for data in datas:
        resultList.append({
            'id': data.id,
            'title': data.title,
            'path': data.path
        })
    return resultList


# ——————————————————————————————————


# ——————————————————————————————————
# 下面是个人中心表单的处理函数:

# dailyReminder表单处理
def solveDailyReminder(dailyReminder):
    if not dailyReminder:
        flash("Please fill in all the required fields", 'error')
        return redirect(url_for('dailyReminderForm'))
    now_time = datetime.now()
    dailyReminder = DailyReminder(datetime=now_time, reminder=dailyReminder)
    db.session.add(dailyReminder)
    db.session.commit()
    flash("success reminder", 'success')
    return


# objectives表单处理
def solveObjectivesForm(medicalAdvice, managementObjectives):
    if not managementObjectives or not medicalAdvice:
        flash("Please fill in all the required fields", 'error')
        return redirect(url_for('dailyReminderForm'))
    now_time = datetime.now()
    objectives = Objectives(datetime=now_time, medical_advice=medicalAdvice, management_objectives=managementObjectives)
    db.session.add(objectives)
    db.session.commit()
    flash("success!!", 'success')
    return


# reports表单处理
def solveReportsForm(hbA1c, insulin, ogtt, insulinTest, cPeptide, diabetesAb, bloodPressure, bloodLipid):
    if not hbA1c or not insulin or not ogtt or not insulinTest or not cPeptide or not diabetesAb or not bloodPressure or not bloodLipid:
        flash("Please fill in all the required fields", 'error')
        return redirect(url_for('reportsForm'))
    now_time = datetime.now()
    reports = HospitalExaminationReports(datetime=now_time,
                                         HbA1c=hbA1c,
                                         insulin=insulin,
                                         OGTT=ogtt,
                                         insulin_releasing_test=insulinTest,
                                         C_peptide_release_test=cPeptide,
                                         Diabetes_associated_antibody=diabetesAb,
                                         blood_pressure=bloodPressure,
                                         blood_lipid=bloodLipid)
    db.session.add(reports)
    db.session.commit()
    flash("Form submitted successfully", 'success')
    return


def solveDailyDataForm(blood_glucose, diet_composition, exercise_amount):
    if not blood_glucose or not diet_composition or not exercise_amount:
        flash("Please fill in all the required fields", 'error')
        return redirect(url_for('dailyDataForm'))

    now_time = datetime.now()
    daily_data = DailyData(datetime=now_time,
                           blood_glucose=blood_glucose,
                           composition_of_Diet=diet_composition,
                           amount_of_exercise=exercise_amount)
    db.session.add(daily_data)
    db.session.commit()

    flash("Form submitted successfully", 'success')
    return


# ——————————————————————————————————


# ——————————————————————————————————
# 下面为个人中心需要的网页资源获取函数
def getDailyReminder():
    reminders = DailyReminder.query.first()
    # 处理一下日期格式
    datetime = str(reminders.datetime)
    datetime = datetime.split(" ")[0]
    print(datetime)
    reminders_data = [{
        'id': reminders.id,
        'datetime': datetime,
        'user_id': reminders.user_id,
        'reminder': reminders.reminder
    }]
    return reminders_data


def getDailyData():
    dailyDatas = DailyData.query.all()
    dailyData = []

    for daily_data in dailyDatas:
        # 处理一下日期格式
        datetime = str(daily_data.datetime)
        datetime = datetime.split(" ")[0]
        dailyData.append({
            'id': daily_data.id,
            'datetime': datetime,
            'user_id': daily_data.user_id,
            'blood_glucose': daily_data.blood_glucose,
            'amount_of_exercise': daily_data.amount_of_exercise,
            'composition_of_Diet': daily_data.composition_of_Diet
        })
    return dailyData
# ——————————————————————————————————
