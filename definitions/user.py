from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, Regexp
from connection import db

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[
        DataRequired(message="Nome é obrigatório"),
        Length(min=3, max=50, message="O nome precisa ter entre 3 e 50 caracteres")
    ])
    email = EmailField('E-mail', validators=[
        DataRequired(message="E-mail é obrigatório"),
        Email(message="Email inválido")
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message="Senha é obrigatória")
    ])

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)