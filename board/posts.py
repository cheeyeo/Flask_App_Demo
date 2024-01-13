from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from board.databaseorm import db
from board.databaseorm import Article, Author


bp = Blueprint('posts', __name__)


@bp.route('/posts/new', methods=['GET'])
@login_required
def new():
    return render_template('posts/create.html')


@bp.route('/posts', methods=['POST'])
@login_required
def create():
    article = Article(
        title=request.form['title'],
        slug=request.form['slug'],
        content=request.form['content'],
        author_id=current_user.id
    )

    db.session.add(article)
    db.session.commit()

    return redirect(url_for("posts.posts"))


@bp.route('/posts')
def posts():
    posts = []

    res = db.session.execute(
        db.select(Article, Author)
        .join(Article.author)
        .order_by(Article.created_on.desc())
    ).all()

    for article, author in res:
        posts.append({
            'title': article.title,
            'content': article.content,
            'created_on': article.created_on,
            'author': f'{author.firstname} {author.lastname}'
        })

    return render_template('posts/posts.html', posts=posts)