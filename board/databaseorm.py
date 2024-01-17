# Using Flask-SQLAlchemy to define db schema

import re
from datetime import datetime
from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


DB = SQLAlchemy(model_class=Base)

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
    

    def fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'


    @validates('firstname')
    def validate_firstname(self, key, firstname):
        if not firstname:
            raise AssertionError('Firstname cannot be blank')
        
        return firstname

      
    @validates('lastame')
    def validate_lastname(self, key, lastname):
        if not lastname:
            raise AssertionError('Lastname cannot be blank')
        
        return lastname


    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email cannot be blank')
        
        if not re.match('[^@]+@[^@]+\.[^@]+', email):
            raise AssertionError('Email not valid format')
        
        return email
    
    # TODO: Validation for password format not working 
    # @validates('password')
    # def validate_password(self, key, password):
    #     if not password:
    #         raise AssertionError('Password cannot be blank')

    #     if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
    #         raise AssertionError('Password must contain 1 capital letter and 1 number')
        
    #     if len(password) < 8 or len(password) > 50:
    #         raise AssertionError('Password must be between 8 and 50 characters')
        
    #     return password


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    created_on: Mapped[Optional[datetime]] = mapped_column(DateTime(), default=datetime.now)
    updated_on: Mapped[Optional[datetime]] = mapped_column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content: Mapped[Text] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(Integer(), ForeignKey("authors.id"), nullable=False)

    author: Mapped[Author] = relationship(back_populates="articles")


    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise AssertionError('Post title cannot be blank!')
        
        return title
    

    @validates('content')
    def validate_content(sef, key, content):
        if not content:
            raise AssertionError('Post content cannot be blank')
        
        return content