"""
该类为数据库模型
"""

from appdir import db


class User(db.Model):
    """用户"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Question(db.Model):
    """论坛问题"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    question = db.Column(db.String(300), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    datetime = db.Column(db.DateTime)

    def __repr__(self):
        return '<Question {}>'.format(self.title)


class Answer(db.Model):
    """论坛回答"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))


class DailyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    blood_glucose = db.Column(db.String(100), index=True)
    amount_of_exercise = db.Column(db.String(100), index=True)
    composition_of_Diet = db.Column(db.String(100), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class HospitalExaminationReports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    HbA1c = db.Column(db.String(100), index=True)
    OGTT = db.Column(db.String(100), index=True)
    insulin = db.Column(db.String(100), index=True)
    insulin_releasing_test = db.Column(db.String(100), index=True)
    C_peptide_release_test = db.Column(db.String(100), index=True)
    Diabetes_associated_antibody = db.Column(db.String(100), index=True)
    blood_pressure = db.Column(db.String(100), index=True)
    blood_lipid = db.Column(db.String(100), index=True)


class DailyReminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reminder = db.Column(db.String(100), index=True)


class Objectives(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    medical_advice = db.Column(db.String(100), index=True)
    management_objectives = db.Column(db.String(100), index=True)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(100), index=True)
    title = db.Column(db.String(100), index=True)
