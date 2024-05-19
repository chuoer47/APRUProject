"""该类存储flask shell命令"""
from datetime import datetime

import click

from appdir import app, db
from appdir.models import User, Article, Question, Answer
from appdir.utils.dataSet import dic_article, forum_data


# 测试shell命令的代码
@app.cli.command("print")
def printf():
    click.echo("hello world")


# 初始化数据库
@app.cli.command("initdb")
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


# 创建一个新用户
@app.cli.command("admin")
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.password = password
    else:
        click.echo('Creating user...')
        user = User(username=username, password=password)
        user.password = password
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')


@app.cli.command("addArticle")
def addArticle():
    for key, v in dic_article.items():
        title = v.split("/")[1]
        title = title.split(".")[0]
        article = Article(id=key, path=v, title=title)
        db.session.add(article)
    db.session.commit()
    click.echo('add articles!')


@app.cli.command("initForum")
def initForum():
    for item in forum_data:
        questionId = item['id']
        question = item['Q']
        title = item['title']
        answers = item['A']
        # 录入问题
        q = Question(id=questionId, title=title, question=question, datetime=datetime.now())
        db.session.add(q)
        for answer in answers:
            a = Answer(content=answer, question_id=questionId)
            db.session.add(a)
        db.session.commit()
    click.echo('init forum success!')
