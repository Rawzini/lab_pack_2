# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru
# Импорт сторонних модулей
import sqlite3
from flask import Flask

from config import config
from routes.post_bp import post_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(post_bp)
