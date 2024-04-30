"""该类存储flask shell命令"""

from appdir import routes, models, app, db
import click
from appdir.models import User


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
