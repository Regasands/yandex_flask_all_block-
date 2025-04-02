from data import db_session
from data.users import User
from datetime import datetime

user1 = User(
    surname="Scott",
    name="Ridley",
    age=21,
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org",
    hashed_password="hashed_password_here", 
    modified_date=datetime.now()
)

user2 = User(
    surname="Johnson",
    name="Mark",
    age=32,
    position="pilot",
    speciality="navigation engineer",
    address="module_2",
    email="mark_johnson@mars.org",
    hashed_password="hashed_password_mark",
    modified_date=datetime.now()
)

user3 = User(
    surname="Williams",
    name="Sarah",
    age=28,
    position="doctor",
    speciality="medical researcher",
    address="module_3",
    email="sarah_w@mars.org",
    hashed_password="hashed_password_sarah",
    modified_date=datetime.now()
)

user4 = User(
    surname="Chen",
    name="Li",
    age=35,
    position="engineer",
    speciality="systems specialist",
    address="module_4",
    email="li_chen@mars.org",
    hashed_password="hashed_password_li",
    modified_date=datetime.now()
)


db_session.global_init('db/blogs.db')
db_sess = db_session.create_session() 
db_sess.add(user1)
db_sess.add(user2)
db_sess.add(user3)
db_sess.add(user4)
db_sess.commit()
