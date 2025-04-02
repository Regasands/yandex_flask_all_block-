from flask import Flask, render_template
from random import choice
import json


app = Flask(__name__)

with open('templates/json.json', 'r', encoding='utf-8') as f:
    direct = json.load(f)['crew']


@app.route('/member')
def get_person():
   person = choice(direct)
   return render_template('list.html', data=person)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
