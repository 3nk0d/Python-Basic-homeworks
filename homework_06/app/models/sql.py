from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(35))
    posts = relationship('Post', back_populates='user')


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    body = Column(String)
    user = relationship('User', back_populates='posts')
