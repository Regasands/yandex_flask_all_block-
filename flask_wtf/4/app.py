from flask import Flask, url_for, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, SubmitField, SelectMultipleField, SelectField, RadioField, TextAreaField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



class RegistrationForm(FlaskForm):
    title = StringField('Название')
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    professions = SelectMultipleField('Какие у вас профессии?', 
                                      choices=[("Инженер-исследователь", "Инженер-исследователь"),
                                               ("Пилот", "Пилот"),
                                               ("Строитель", "Строитель"),
                                               ("Экзобиолог", "Экзобиолог"),
                                               ("Врач", "Врач"),
                                               ("Инженер по терраформированию", "Инженер по терраформированию"),
                                               ("Климатолог", "Климатолог"),
                                               ("Специалист по радиационной защите", "Специалист по радиационной защите"),
                                               ("Астрогеолог", "Астрогеолог"),
                                               ("Гляциолог", "Гляциолог"),
                                               ("Инженер жизнеобеспечения", "Инженер жизнеобеспечения"),
                                               ("Метеоролог", "Метеоролог"),
                                               ("Оператор марсохода", "Оператор марсохода"),
                                               ("Киберинженер", "Киберинженер"),
                                               ("Штурман", "Штурман"),
                                               ("Пилот дронов", "Пилот дронов")])
    education = SelectField('Какое у вас образование?', 
                            choices=[("primary", "Начальное"),
                                     ("secondary", "Среднее"),
                                     ("higher", "Высшее")])
    sex = RadioField('Укажите пол', 
                     choices=[("male", "Мужской"), ("female", "Женский")], 
                     default="male")
    about = TextAreaField('Немного о себе')
    photo = FileField('Приложите фотографию')
    accept = BooleanField('Готовы остаться на Марсе?')
    submit = SubmitField('Записаться')




@app.route('/astronaut_selection', methods=['POST', "GET"])
def gregister():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('answer', 
                                title=form.title.data, 
                                surname=form.surname.data,
                                name=form.name.data, 
                                education=form.education.data, 
                                profession=",".join(form.professions.data), 
                                sex=form.sex.data, 
                                motivation=form.about.data, 
                                ready=form.accept.data))
    return render_template('data.html', form=form)


@app.route('/answer')
def answer():
    data = {
        "title": request.args.get('title', ''),
        "surname": request.args.get('surname', ''),
        "name": request.args.get('name', ''),
        "education": request.args.get('education', ''),
        "profession": request.args.get('profession', '').split(','),  
        "sex": request.args.get('sex', ''),
        "motivation": request.args.get('motivation', ''),
        "ready": request.args.get('ready', 'False') == 'True'  
    }
    return render_template('html.html', css_url=url_for('static', filename='css/base.css'), data=data)

@app.route('/answer_auto')
def answer_auto():
    data = {'title': 'sa', 'surname': 'df', 'name': 'namee', 'education': 'none', 'profession': 'as', 'sex': 'none', 'motivaiotn': 'none', 'ready': "Yes"}
    return render_template('html.html', css_url=url_for('static', filename='css/base.css'), data=data)

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
