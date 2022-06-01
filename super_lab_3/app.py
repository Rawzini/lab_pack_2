# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru
# Импорт сторонних модулей
import sqlite3
from flask import Flask

from config import config
from routes.routes import routes
from models.basic import db

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(routes)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
