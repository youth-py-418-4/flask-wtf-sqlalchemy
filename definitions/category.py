from connection import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CategoryForm(FlaskForm):
    label = StringField('Nome', [
        DataRequired(),
        Length(min=3, max=20)
    ])

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)
