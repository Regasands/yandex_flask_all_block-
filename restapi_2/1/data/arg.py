from flask_restful import reqparse


class UserParser:
    @staticmethod
    def get_all_arg():
        parser = reqparse.RequestParser()
        parser.add_argument('surname', type=str, required=False, 
                          help='Фамилия пользователя (необязательно)')
        parser.add_argument('name', type=str, required=True,
                          help='Имя пользователя (обязательно)')
        parser.add_argument('age', type=int, required=False,
                          help='Возраст (целое число, необязательно)')
        parser.add_argument('position', type=str, required=False,
                          help='Должность (необязательно)')
        parser.add_argument('speciality', type=str, required=False,
                          help='Специальность (необязательно)')
        parser.add_argument('address', type=str, required=False,
                          help='Адрес (необязательно)')
        parser.add_argument('email', type=str, required=True,
                          help='Email (обязательно, уникальный)', 
                          trim=True)
        parser.add_argument('hashed_password', type=str, required=True,
                          help='Пароль (обязательно)')
        
        return parser


