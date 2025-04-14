from flask import Flask
from data.api_user import blueprint
from data.db_session import global_init

app = Flask(__name__)
global_init('db/user.db')
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

