from flask import Flask

from config import config
from models.user import User
from routes.routes import routes
from global_objects import db, login_manager

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(routes)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'routes.login'

@app.before_first_request
def create_tables():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

if __name__ == '__main__':
    app.run(debug=True)
