from sql import User, Post, read_user, read_users, read_record, read_records, Session
from sqlalchemy.orm import Session as SessionType


def view_records_users():
    session: SessionType = Session()

    users = read_users(session)

    #session.close()
    return users

#read()