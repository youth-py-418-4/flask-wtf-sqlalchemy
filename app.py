from flask import Flask
from flask_login import LoginManager
from routes.auth import auth_routes
from routes.dashboard import dashboard_routes
from routes.posts import post_routes
from routes.categories import category_routes
from connection import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qualquer-coisa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Apenas em desenvolvimento
app.config['SESSION_COOKIE_SECURE'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Você precisa estar logado para ver essa página'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    from definitions.user import User
    return User.query.get(int(user_id))

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(dashboard_routes)
app.register_blueprint(post_routes, url_prefix='/dashboard/posts')
app.register_blueprint(category_routes, url_prefix='/dashboard/categories')

with app.app_context():
    db.create_all()

app.run(debug=True)