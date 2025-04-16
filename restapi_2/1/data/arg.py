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

class JobsParser:
    @staticmethod
    def get_all_arg():
        parser = reqparse.RequestParser()
        job_parser = reqparse.RequestParser()
        job_parser.add_argument('team_leader', type=int, required=True, help='Team leader ID is required and must be an integer')
        job_parser.add_argument('job', type=str, required=True, help='Job description is required')
        job_parser.add_argument('work_size', type=int, required=True, help='Work size is required and must be an integer')
        job_parser.add_argument('collaborators', type=list, location='json', required=False, help='Collaborators should be a list of user IDs')
        job_parser.add_argument('start_date', type=str, required=False, help='Start date should be a string in ISO format')
        job_parser.add_argument('end_date', type=str, required=False, help='End date should be a string in ISO format')
        job_parser.add_argument('is_finished', type=bool, required=False, help='is_finished should be a boolean')
        return parser  
