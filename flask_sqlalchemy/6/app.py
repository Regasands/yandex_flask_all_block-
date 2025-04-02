import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data.db_session import *


name = input()
global_init(name)

session = create_session()

for user in session.query(User).filter(User.address == 'module_1', ~User.speciality.like('%engineer%'), ~User.position.like('%engineer%')):
    print(user.id)
