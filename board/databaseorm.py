# Using Flask-SQLAlchemy to define db schema

from datetime import datetime
from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Author(UserMixin, Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    joined: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now)

    articles: Mapped[List["Article"]] = relationship(back_populates='author')

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, email={self.email!r}, fullname={self.firstname!r} {self.lastname!r})"
    

    @property
    def is_active(self):
        return True



class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    created_on: Mapped[Optional[datetime]] = mapped_column(DateTime(), default=datetime.now)
    updated_on: Mapped[Optional[datetime]] = mapped_column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content: Mapped[Text] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(Integer(), ForeignKey("authors.id"), nullable=False)

    author: Mapped[Author] = relationship(back_populates="articles")


