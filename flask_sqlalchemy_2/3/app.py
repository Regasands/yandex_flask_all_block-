from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm

from wtforms import PasswordField, StringField, IntegerField, SubmitField, DateTimeField, BooleanField, FieldList
from wtforms.validators import DataRequired, Email, Length, Optional
from werkzeug.security import generate_password_hash

from data.db_session import global_init, create_session

from flask_login import LoginManager, login_required, login_user, current_user, logout_user

from data.marsone import User, Jobs

from werkzeug.security import check_password_hash

import datetime


def create_user_from_form(form):
    # Получаем словарь из формы
    form_data = form.data.copy()

    # Удаляем лишние поля
    form_data.pop('csrf_token', None)
    form_data.pop('submit', None)

    # Обрабатываем пароль
    if 'password' in form_data:
        form_data['hashed_password'] = generate_password_hash(
            form_data.pop('password'))

    # Возвращаем готовый объект пользователя
    return User(**form_data)


global_init('db/info.db')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'beta_gama_beta'
login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[Optional(), Length(max=50)])
    name = StringField('Имя', validators=[Optional(), Length(max=50)])
    age = IntegerField('Возраст', validators=[Optional()])
    position = StringField('Должность', validators=[
                           Optional(), Length(max=100)])
    speciality = StringField('Специальность', validators=[
                             Optional(), Length(max=100)])
    address = StringField('Адрес', validators=[Optional(), Length(max=200)])
    email = StringField('Email', validators=[
                        DataRequired(), Length(max=120)])
    password = PasswordField('Пароль', validators=[
                             DataRequired(), Length(min=6)])
    submit = SubmitField('Зарегистрироваться/Войти')


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and check_password_hash(user.hashed_password, form.password.data):
            login_user(user, remember=True)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
def home():
    ses = create_session()
    if current_user.is_authenticated:
        jobs = ses.query(Jobs).all()
        return render_template('home.html', jobs=jobs, current_user=current_user)
    else:
        return redirect('/login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    ses = create_session()
    if form.validate_on_submit():
        try:
            has_data = ses.query(User).filter(
                User.email == form.email.data).all()
            if has_data:
                print(has_data)
                return render_template('registet.html',
                                       message='такие данные уже есть', form=form)
            else:
                user = create_user_from_form(form)
                ses.add(user)
                ses.commit()
                return redirect('/login')
        except Exception as e:
            print(e)
            return redirect('/register')
    return render_template('register.html', form=form)


class JobForm(FlaskForm):
    job = StringField('Job Description', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = FieldList(StringField('Collaborator'), min_entries=1)
    start_date = DateTimeField(
        'Start Date', default=datetime.datetime.now, validators=[DataRequired()])
    end_date = DateTimeField(
        'End Date', default=datetime.datetime.now(), validators=[Optional()])
    is_finished = BooleanField('Is Finished', default=False)
    submit = SubmitField('Отправить')


@app.route('/addjob', methods=['POST', 'GET'])
def addjob():
    form = JobForm()
    if form.validate_on_submit():
        try:
            ses = create_session()
            new_job = Jobs(
                team_leader=current_user.id,
                job=form.job.data,
                work_size=form.work_size.data,
                collaborators=form.collaborators.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                is_finished=form.is_finished.data
            )

            ses.add(new_job)
            ses.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/addjob')
    return render_template('addjobs.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
