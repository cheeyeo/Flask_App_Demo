from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import Session
from postgresql.testmigrations import Article, Author


if __name__ == "__main__":
    engine = create_engine(
        "postgresql+psycopg2://chee:example@172.18.0.2/example",
        echo=True
    )

    with Session(engine) as session:
        ezz = Author(
            firstname="Ezzeddin",
            lastname="Abdullah",
            email="ezz_email@gmail.com"
        )

        ahmed = Author(
            firstname="Ahmed",
            lastname="Mohammed",
            email="ahmed_email@gmail.com"
        )

        article = Article(
            slug='clean-python2',
            title='How to write clean python',
            content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            author=ezz
        )

        session.add(article)
        session.commit()

        print(article.title)

        article2 = Article(
            slug="postgresql-system-catalogs-metadata",
            title="How to Get Metadata from PostgreSQL System Catalogs",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            created_on = datetime(2022, 8, 29),
            author=ezz
        )

        article3 = Article(
            slug="sqlalchemy-postgres",
            title="Interacting with Databases using SQLAlchemy with PostgreSQL",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            author=ahmed
        )

        session.add(article2)
        session.add(article3)
        session.commit()
        