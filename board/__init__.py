from flask import Flask
from board import pages, posts
from board.databaseorm import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://chee:example@172.18.0.2:5432/example'
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    
    return app