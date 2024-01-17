import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from board import author, pages, posts, errors
from board.databaseorm import DB, Base, Author


load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    
    # Setup db
    DB.init_app(app)

    with app.app_context():
        DB.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'author.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # print(f'INSIDE LOAD USER: {user_id}')
        user = DB.session.execute(
            DB.select(Author)
            .filter_by(id=user_id)
        ).scalar()
    
        return user


    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(author.bp)
    app.register_error_handler(404, errors.page_not_found)
    
    return app