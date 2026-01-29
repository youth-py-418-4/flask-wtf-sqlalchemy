from flask import Flask
from routes.auth import auth_routes
from connection import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qualquer-coisa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(auth_routes, url_prefix='/auth')

with app.app_context():
    db.create_all()

app.run(debug=True)