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

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(
    url=PG_CONN_URI,
    echo=True
)

Base = declarative_base(bind=engine)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class User(Base):
    name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(35))
    posts = relationship('Post', back_populates='User')


class Post(Base):
    user_id = Column(Integer)
    title = Column(String)
    body = Column(String)
    user = relationship('User', back_populates='Post')