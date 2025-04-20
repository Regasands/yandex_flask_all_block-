import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from .marsone import SqlAlchemyBase

__factory = None

def global_init(db_path):
    global __factory

    if __factory:
        return

    connection_str = f'sqlite:///{db_path}?check_same_thread=False'
    print(f"Connecting {connection_str}")

    engine = sa.create_engine(connection_str, echo=False)
    __factory = sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)

def create_session():
    global __factory
    return __factory()

