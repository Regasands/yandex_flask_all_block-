from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
f = lambda x: url_for('static', filename=f'img/{x}')
si1p = ['1.png', '2.png', '3.png']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/img'

class FirstForm(FlaskForm):
    file = FileField('вставь сюда изображение')
    submit = SubmitField('отправить')

@app.route('/galery', methods=['GET', 'POST'])
def load_photo():
    form = FirstForm()
    if form.validate_on_submit():
        file = request.files.get('file') 
        if file and file.name:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            si1p.append(file.filename)
            print(file)
        else:
            print(file)
    sp = [f(i) for i in si1p]
    return render_template('beta.html', form=form, elems=sp)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
