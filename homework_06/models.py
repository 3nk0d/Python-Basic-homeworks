"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")

engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)

Base = declarative_base(bind=engine)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(35))
    posts = relationship('Post', back_populates='user')


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    body = Column(String)
    user = relationship('User', back_populates='posts')
