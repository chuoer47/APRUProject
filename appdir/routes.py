from appdir import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return render_template('base.html')


@app.route('/index', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')
