from flask_sqlalchemy import SQLAlchemy
import os

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+psycopg2://postgres:super@localhost/postgres"

db = SQLAlchemy()
