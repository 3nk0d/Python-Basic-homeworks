from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker, relationship, Session as SessionType
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import os
from .database import db

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+psycopg2://postgres:super@localhost/postgres"

engine = create_engine(url=PG_CONN_URI, echo=True)

Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(35))
    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return f"Post(id={self.id}, name={self.name!r}, username = {self.username}, email = {self.email}, posts = {self.posts})"

    def __repr__(self):
        return str(self)


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    body = Column(String)
    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r}, body = {self.body}, user = {self.user})"

    def __repr__(self):
        return str(self)


def read_record(session: SessionType, post_id) -> Post | None:
    post = session.query(Post).filter_by(id=post_id).one_or_none()
    #print(post)
    return post


def read_records(session: SessionType) -> Post | None:
    posts = session.query(Post).all()
    #print(post)
    return posts


def read_user(session: SessionType, user_id) -> User | None:
    user = session.query(User).filter_by(id=user_id).one_or_none()
    #print(user)
    return user


def read_users(session: SessionType) -> User | None:
    users = session.query(User).all()
    #print(user)
    return users


def create_user(data, session: SessionType):
    user = User(id=item.get("id"), name=item.get("name"), username=item.get("username"), email=item.get("email"))
    session.add(user)
    session.commit()


def create_posts(data, session: SessionType):
    post = Post(id=item.get("id"), user_id=item.get("userId"), title=item.get("title"), body=item.get("body"))
    session.add(post)
    session.commit()
