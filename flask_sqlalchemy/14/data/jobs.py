import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(
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
