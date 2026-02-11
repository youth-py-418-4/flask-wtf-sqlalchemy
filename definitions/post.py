from connection import db
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Titulo', [
        DataRequired(),
        Length(max=50)
    ])
    content = StringField('Conteúdo', [
        DataRequired(),
        Length(max=500)
    ])
    category = SelectField('Categoria', [
        DataRequired()
    ])

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
