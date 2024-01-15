from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from board import author, pages, posts
from board.databaseorm import db, Author


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'example-secret-key'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://chee:example@172.18.0.2:5432/example'
    
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'author.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        print(f'INSIDE LOAD USER: {user_id}')
        user = db.session.execute(
            db.select(Author)
            .filter_by(id=user_id)
        ).scalar_one()
    
        return user


    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(author.bp)
    
    return app