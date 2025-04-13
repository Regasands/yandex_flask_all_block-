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

for user in session.query(User).filter(User.age < 18):
    print(user, user.age, 'years')
