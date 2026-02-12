from flask import Blueprint, render_template, flash
from definitions.post import Post, PostForm
from definitions.category import Category
from connection import db
from flask_login import current_user

post_routes = Blueprint('posts', __name__)

@post_routes.route('/', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    categories = Category.query.all()

    form.category.choices = []
    for category in categories:
        form.category.choices.append((category.id, category.label))

    if form.validate_on_submit():
        post = Post(
            author=current_user.id,
            title=form.title.data,
            content=form.content.data,
            category=int(form.category.data)
        )
        db.session.add(post)
        db.session.commit()
        flash('Post criado com sucesso', 'success')

    posts = Post.query.all()
    return render_template('posts_lista.html', posts=posts, form=form)
