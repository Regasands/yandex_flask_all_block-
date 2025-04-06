from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class RegistrionForm(FlaskForm):
    name = StringField('Login / email')
    password = PasswordField('Password')
    password_repeat = PasswordField('Confirm Password',
                                    validators=[EqualTo('password', message='Пароли не совпадают')])
    surname = StringField('Surname')
    name_1 = StringField('Name')
    age = IntegerField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
    submit = SubmitField('Записаться')


@app.route('/register', methods=['POST', "GET"])
def register():
    form = RegistrionForm()
    if form.validate_on_submit():
        return 'h1'
    return render_template('list.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
