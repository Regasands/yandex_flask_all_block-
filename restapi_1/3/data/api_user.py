import flask
from .users import User
from .db_session import create_session
from flask import make_response, jsonify, render_template, request
from io import BytesIO
import requests
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

blueprint =  flask.Blueprint('user_api', __name__, template_folder='templates')

@blueprint.route('/users_show/<int:id_user>')
def get_sity(id_user):
    ses = create_session()
    user = ses.query(User).get(id_user)
    if not user:
        return make_response(jsonify({'error': 'not_find_user'}), 400)

    koord = user.city_kord.split('f')

    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_api_server = "https://static-maps.yandex.ru/v1?"
    
    params = {'ll': f'{koord[1]},{koord[0]}', 'spn': f'0.1,0.1',  'apikey': apikey, 'lang': 'ru_Ru'}
    response = requests.get(map_api_server, params=params)
    print(response.url)
    image = BytesIO(response.content)

    map_base64 = base64.b64encode(image.getvalue()).decode('utf-8')
    return render_template(
        'user_city.html',
        user=user,
        map_image=f"data:image/jpeg;base64,{map_base64}"
    )
    
@blueprint.route('/add_user', methods=['POST'])
def add_user(): 
    sp = ('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password', 'modified_date', 'city_form', 'city_kord')
    if not request.json:
        return make_response(jsonify({'error': 'need data'}), 400)

    elif not all(key in request.json for key in sp):
        return make_response(jsonify({'errors': 'neeed_moredata'}), 400)

    try:

        ses = create_session()
        a = request.json.get('city_kord').split()
        a = f'{a[0]}f{a[1]}'
        new_user = User(
            surname=request.json.get('surname'),  # .get() вместо [], чтобы не было KeyError, если поля нет
            name=request.json.get('name'),
            age=request.json['age'],
            position=request.json['position'],
            speciality=request.json['speciality'],
            address=request.json.get('address'),
            email=request.json.get('email'),
            hashed_password=generate_password_hash(request.json.get('hashed_password')),
            modified_date=datetime.fromisoformat(request.json['modified_date']) if 'modified_date' in request.json else None,
            city_form = request.json.get('city_form'),
            city_kord = a,
        )
        ses.add(new_user)
        ses.commit()
        return jsonify({'id': new_user.id})
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
