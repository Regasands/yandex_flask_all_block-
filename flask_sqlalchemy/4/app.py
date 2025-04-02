import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data.db_session import *
from data.jobs import Jobs
global_init('db/blogs.db')
from datetime import datetime

def add_sample_jobs():
    session = create_session()
    
    job1 = Jobs(
        team_leader=1,
        job="deployment of residential modules 1 and 2",
        work_size=15,
        collaborators=[2, 3],
        start_date=datetime.now(),
        is_finished=False
    )
    
    job2 = Jobs(
        team_leader=2,
        job="installation of solar panels",
        work_size=20,
        collaborators=[1, 4],
        start_date=datetime.now(),
        is_finished=True,
        end_date=datetime.now()
    )
    
    job3 = Jobs(
        team_leader=3,
        job="life support systems check",
        work_size=8,
        collaborators=[1, 2],
        start_date=datetime.now(),
        is_finished=False
    )
    
    job4 = Jobs(
        team_leader=1,
        job="scientific experiments",
        work_size=30,
        collaborators=[2, 3, 4],
        start_date=datetime.now(),
        is_finished=False
    )
    
    session.add_all([job1, job2, job3, job4])
    session.commit()
    session.close()

if __name__ == '__main__':
    add_sample_jobs()
