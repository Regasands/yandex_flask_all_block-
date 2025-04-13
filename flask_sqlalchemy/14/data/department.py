import sqlalchemy as chemy
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):

    __tablename__ = 'department'
    id = chemy.Column(chemy.Integer, primary_key=True, autoincrement=True)
    title = chemy.Column(chemy.String)
    chief = chemy.Column(chemy.Integer, chemy.ForeignKey('users.id'))
    members = chemy.Column(chemy.JSON)
    email = chemy.Column(chemy.String)

    user = orm.relationship("User", back_populates="department")
