from flask import Blueprint, render_template, redirect, flash
from flask_login import login_user, logout_user, current_user
from definitions.user import RegisterForm, User, LoginForm
from connection import db

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect('/dashboard')
        else:
            flash("Email ou senha incorretos", "danger")

    return render_template('login.html', form=form)

@auth_routes.route('/logout')
def logout():
    logout_user()
    flash("Você saiu da sua conta", "info")
    return redirect("/auth/login")

@auth_routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if current_user.is_authenticated:
        return redirect('/dashboard')

    if form.validate_on_submit():
        user = User(
            name = form.name.data,
            email = form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registrado com sucesso, você pode fazer login", "success")
        return redirect('/auth/login')

    users = User.query.all()

    return render_template('register.html', form=form, users=users)

@auth_routes.route('/forgot')
def forgot():
    return 'Esqueci minha senha'

