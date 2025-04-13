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
session = create_session()
max_ = 0
for elem in session.query(Jobs).all():
   max_ = len(elem.collaborators) if len(elem.collaborators) > max_ else max_

for elem in session.query(Jobs).all():
    if len(elem.collaborators) == max_:
        print(elem.user.name, elem.user.surname)
