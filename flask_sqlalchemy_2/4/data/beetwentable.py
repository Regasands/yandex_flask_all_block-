import  sqlalchemy as sa
import sqlalchemy.orm as orm
from .db_session import SqlAlchemyBase


association_table = sa.Table(
    'assorciattion',
    SqlAlchemyBase.metadata,
    sa.Column('jobs', sa.Integer, sa.ForeignKey('jobs.id')),
    sa.Column('categorywork', sa.Integer, sa.ForeignKey('categorywork.id'))

)

class Catrgorty(SqlAlchemyBase):
    __tablename__ = 'categorywork'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name_int = sa.Column(sa.Integer)
    job = orm.relationship("Jobs", secondary='assorciattion', backref='cat')

