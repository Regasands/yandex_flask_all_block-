from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<string:title>')
def test(title):
    return render_template('html.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
