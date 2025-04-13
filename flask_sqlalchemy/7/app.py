import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data.db_session import *
from data.jobs import Jobs

from flask import Flask, render_template


global_init('db/blogs.db')

app = Flask(__name__)


@app.route('/')
def start_home():
    session = create_session()
    data = session.query(Jobs).all()
    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
