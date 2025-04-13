from flask import Flask, render_template


app = Flask(__name__)

@app.route('/table/<string:sex>/<int:age>')
def get_data(sex, age):
    return render_template('list.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
