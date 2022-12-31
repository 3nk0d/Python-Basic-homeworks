from homework_06.models.sql import read_users, Session
from sqlalchemy.orm import Session as SessionType


def view_records_users():
    session: SessionType = Session()

    users = read_users(session)

    #session.close()
    return users

#read()