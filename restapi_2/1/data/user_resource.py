from flask import jsonify
from flask_restful import Resource, abort
from .db_session import create_session
from .models import User
from .arg import UserParser
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class UsersResource(Resource):
    def get(self, user_id):
        try:
            ses = create_session()
            sp = ('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date')
            user = ses.query(User).get(user_id)
            if not user:
                abort(404, message='User not found')
            return {
                'user': user.to_dict(only=sp)
            }
        except Exception as e:
            abort(404, message=f'error {e}')

    def delete(self, user_id):
        ses = create_session()
        try:
            user = ses.query(User).get(user_id)
            if not user:
                return abort(404, message='pls send corret id')
            ses.delete(user)
            ses.commit()
            return {'success': 'ok'}
        except Exception as e:
            abort(404, message='error')

    def put(self, user_id):
        ses = create_session()
        try:
            user = ses.query(User).get(user_id)


            parser = UserParser().get_all_arg()
            args = parser.parse_args()


            user.surname = args.get('surname', user.surname) 
            user.name = args.get('name', user.name)
            user.age = args.get('age', user.age)
            user.position = args.get('position', user.position)
            user.speciality = args.get('speciality', user.speciality)
            user.address = args.get('address', user.address)

            if 'email' in args and args['email'] != user.email:

                if ses.query(User).filter(User.email == args['email']).first():
                    abort(400, message="Email already exists")
                user.email = args['email']

            if 'hashed_password' in args:
                user.hashed_password = generate_password_hash(args['hashed_password'])

            user.modified_date = datetime.utcnow() 
            ses.commit()
            return {'message': 'User updated successfully'}
        except Exception as e:
            abort(500, message=f'new error {e}')



class UsersListResource(Resource):
    def get(self):
        ses = create_session()
        users = ses.query(User).all()

        sp = ('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date')
        return jsonify({
            'users':
                [item.to_dict(only=sp) for item in users]
        })

    def post(self):
        ses = create_session()
        try:
            
            parser = UserParser().get_all_arg()
            args = parser.parse_args()
            parser = UserParser.get_all_arg()
            args = parser.parse_args()
            
            required_fields = ['name', 'email', 'hashed_password']
            for field in required_fields:
                if not args.get(field):
                    abort(400, message=f"{field} is required")
            
            if ses.query(User).filter(User.email == args['email']).first():
                abort(400, message="Email already exists")
            
            new_user = User(
                surname=args.get('surname'),
                name=args['name'],
                age=args.get('age'),
                position=args.get('position'),
                speciality=args.get('speciality'),
                address=args.get('address'),
                email=args['email'],
                hashed_password=generate_password_hash(args['hashed_password']),
                modified_date=datetime.now())
            ses.add(new_user)
            ses.commit()
            return {'ses': f'{new_user.id}'}
            
        except Exception as e:
            abort(500, message=f'new error {e}')


