from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

SqlAlchemyBase = declarative_base()

job_category_association = sa.Table(
    'job_category_association',
    SqlAlchemyBase.metadata,
    sa.Column('job_id', sa.Integer, sa.ForeignKey('jobs.id')),
    sa.Column('category_id', sa.Integer, sa.ForeignKey('job_categories.id'))
)

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String(50))
    name = sa.Column(sa.String(50))
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String(100))
    speciality = sa.Column(sa.String(100))
    address = sa.Column(sa.String(200))
    email = sa.Column(sa.String(120), index=True, unique=True)
    hashed_password = sa.Column(sa.String(128))
    modified_date = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)

    jobs = orm.relationship("Jobs", back_populates="user")
    departments = orm.relationship("Department", back_populates="user")

class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    job = sa.Column(sa.String(200))
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.JSON)
    start_date = sa.Column(sa.DateTime, default=datetime.now)
    end_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean, default=False)

    user = orm.relationship("User", back_populates="jobs")
    categories = orm.relationship("JobCategory", secondary=job_category_association, back_populates="jobs")

class JobCategory(SqlAlchemyBase):
    __tablename__ = 'job_categories'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)

    jobs = orm.relationship("Jobs", secondary=job_category_association, back_populates="categories")

class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    members = sa.Column(sa.JSON)
    email = sa.Column(sa.String)

    user = orm.relationship("User", back_populates="departments")

