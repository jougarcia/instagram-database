import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__='follower'
    id = Column(Integer, primary_key=True)
    from_id=Column(Integer,ForeignKey('user.id'))
    From_user=relationship("User",backref='user')
    to_id=Column(Integer,ForeignKey('user.id'))
    to_user=relationship("User",backref='user')

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    comment = relationship('Comment', backref='user', lazy=True)
    post = relationship('Post', backref='user', lazy=True)
    follower = relationship('Follower', backref='user', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column (Integer,primary_key=True)
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    type =Column(String(250))
    url =Column(String(250))
    post_id = Column(Integer,ForeignKey('post.id'))

    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
