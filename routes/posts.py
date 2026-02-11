from flask import Blueprint, render_template
from definitions.post import Post
post_routes = Blueprint('posts', __name__)

@post_routes.route('/')
def posts():
    posts = Post.query.all()

    return render_template('posts_lista.html', posts=posts)
