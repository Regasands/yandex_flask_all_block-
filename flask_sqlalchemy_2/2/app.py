from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField

from data.db_session import global_init, create_session

from flask_login import LoginManager, login_user

from data.marsone import User

global_init('db/new.db')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'beta_gama_beta'
login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    login = StringField('Логин')
    password = PasswordField('Пароль')
    telegram_nick = StringField('Telegram ник')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(
            User.telegram_nick == form.telegram_nick.data).first()
        if user:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
