from flask import Flask

app = Flask(__name__)

from appdir import routes, models
