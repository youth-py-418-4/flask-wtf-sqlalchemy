from flask import Blueprint, render_template
from definitions.user import RegisterForm, User
from connection import db

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login')
def login():
    return 'Login'

@auth_routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    message = ''
    if form.validate_on_submit():
        user = User(
            name = form.name.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        message = "Form enviado com sucesso"

    users = User.query.all()

    return render_template('register.html', form=form, message=message, users=users)

@auth_routes.route('/forgot')
def forgot():
    return 'Esqueci minha senha'

