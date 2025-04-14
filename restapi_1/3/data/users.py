
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String(100))
    speciality = sqlalchemy.Column(sqlalchemy.String(100))
    address = sqlalchemy.Column(sqlalchemy.String(200))
    email = sqlalchemy.Column(sqlalchemy.String(
        120), index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String(128), nullable=True)
    modified_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )
    city_form = sqlalchemy.Column(sqlalchemy.String)
    city_kord = sqlalchemy.Column(sqlalchemy.String)
