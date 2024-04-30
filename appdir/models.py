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
    description = db.Column(db.String(300), index=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Question {}>'.format(self.title)


class Answer(db.Model):
    """论坛回答"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), index=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
