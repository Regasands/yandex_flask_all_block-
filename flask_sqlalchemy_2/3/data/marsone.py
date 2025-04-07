import sqlalchemy as sa
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime
from sqlalchemy import orm


class User(SqlAlchemyBase, UserMixin):
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
    jobs = orm.relationship("Jobs", back_populates="user")


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.id'),
        nullable=False)
    job = sqlalchemy.Column(sqlalchemy.String(200))
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.JSON)
    start_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False
    )

    user = orm.relationship("User", back_populates="jobs")
