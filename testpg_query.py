from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from postgresql.testmigrations import Article, Author


if __name__ == '__main__':
     engine = create_engine(
        "postgresql+psycopg2://chee:example@172.18.0.2/example",
        echo=True
    )
     
     with Session(engine) as session:
          articles = session.query(Article)

          for article in articles:
               print(article.id, article.title)
          

          for article in session.query(Article).order_by(Article.created_on.desc()):
               print(article.title)

          article_query = session.query(Article).filter(Article.slug == 'clean-python2')


          article_query.update({'title': 'TEST sss'})
          print(article_query.first().title)

          session.commit()

          print()
          print('Testing query of articles...')
          article = article_query.first()
          print(article)
          print(article.author)

          print()
          print('Test query of author...')
          author_query = session.query(Author)
          author = author_query.first()
          author_articles = author.articles
          author_articles = [(ar.id, ar.title) for ar in author_articles]
          print(f'Author: {author}')
          print(f'Articles: {author_articles}')