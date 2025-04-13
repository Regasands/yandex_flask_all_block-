from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class Login(FlaskForm):
    id_a = IntegerField('Id астронавта')
    passeord_a = PasswordField('пароль астронавта')
    id_b = IntegerField('Id капитана')
    passeord_b = PasswordField('пароль капитана')       
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        return 'SUBMIT'
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

