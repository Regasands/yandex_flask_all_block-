import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()
__factory = None


def global_init(db_file):
    global __factory
    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception('Need cohose file')

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


name = input()
global_init(name)
ses = create_session()

for elem in ses.query(Department).get(1).members:
    user = ses.query(User).get(elem)
    if not user:
        continue
    job = ses.query(Jobs).filter(Jobs.team_leader == user.id).all()
    h = sum(int(jobs.work_size) for jobs in job)
    print(user.surname, user.name)
    name)
