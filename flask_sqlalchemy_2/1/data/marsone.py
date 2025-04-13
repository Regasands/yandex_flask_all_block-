import sqlalchemy as sa
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    telegram_nick = sa.Column(sa.String, unique=True)
