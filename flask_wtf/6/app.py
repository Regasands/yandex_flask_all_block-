from flask import Flask, render_template

app = Flask(__name__)

@app.route('/distribution')
def distribution():
    astronauts = [
        {'name': 'Капитан', 'role': 'Капитан'},
        {'name': 'Мария', 'role': 'Инженер'},
        {'name': 'Дмитрий', 'role': 'Пилот'},
        {'name': 'Анна', 'role': 'Медик'}
    ]
    return render_template('list.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
