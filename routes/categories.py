from flask import Blueprint, render_template, flash
from definitions.category import Category, CategoryForm
from connection import db
category_routes = Blueprint('categories', __name__)

@category_routes.route('/', methods=['GET', 'POST'])
def categories():
    form = CategoryForm()

    if form.validate_on_submit():
        category = Category(label=form.label.data)
        db.session.add(category)
        db.session.commit()
        flash('Categoria cadastrada com sucesso', 'success')

    categories = Category.query.all()

    return render_template('categories_lista.html', categories=categories, form=form)
