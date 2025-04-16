from  flask_restful import abort, Resource
from .db_session import create_session
from .models import Jobs
from .arg import JobsParser
from datetime import datetime

class JobsResource(Resource):
    def get(self, jobs_id):
        try:
            ses = create_session()
            sp = ('id', 'job', 'work_size', 'team_leader', 'collaborators', 'start_date', 'end_date', 'is_finished')                
            job = ses.query(Jobs).get(jobs_id)
            if not job:
                abort(404, message='not found')
            return {
                'job': job.to_dict(only=sp)
            }
        except Exception as e:
            abort(404, message=f'error {e}')

    def delete(self, jobs_id):
        ses = create_session()
        try:
            jobs = ses.query(Jobs).get(jobs_id)
            if not jobs:
                return abort(404, message='pls send corret id')
            ses.delete(jobs)
            ses.commit()
            return {'success': 'ok'}
        except Exception as e:
            abort(404, message='error')

    def put(self, jobs_id):
        ses = create_session()
        try:
            job = ses.query(Jobs).get(jobs_id)
            if not job:
                abort(400, message='not found')


            parser = JobsParser().get_all_arg()
            args = parser.parse_args()


            job.team_leader = args.get('team_leader', job.team_leader)
            job.job = args.get('job', job.job)
            job.work_size = args.get('work_size', job.work_size)
            job.collaborators = args.get('collaborators', job.collaborators)
            job.start_date = args.get('start_date', job.start_date)
            job.end_date = args.get('end_date', job.end_date)
            job.is_finished = args.get('is_finished', job.is_finished)

            ses.commit()
            return {'message': 'User updated successfully'}
        except Exception as e:
            abort(500, message=f'new error {e}')


class JobsListResource(Resource):
    def get(self):
        try:
            print('1')
            ses = create_session()
            sp = ('id', 'job', 'work_size', 'team_leader', 'collaborators', 'start_date', 'end_date', 'is_finished')               
            jobs = ses.query(Jobs).all()

            return {
                'jobs': [job.to_dict(only=sp) for job in jobs]
            }
        except Exception as e:
            abort(404, message=f'error {e}')

    def post(self):
        ses = create_session()
        try:
            parser = JobsParser().get_all_arg()
            args = parser.parse_args()
            job = Jobs(
                team_leader=args['team_leader'],
                job=args['job'],
                work_size=args['work_size'],
                collaborators=args.get('collaborators', []),
                start_date=datetime.fromisoformat(args['start_date']) if args.get('start_date') else datetime.now(),
                end_date=datetime.fromisoformat(args['end_date']) if args.get('end_date') else None,
                is_finished=args.get('is_finished', False)
            )
            ses.add(job)
            ses.commit()
            return {'message': 'User updated successfully'}

        except Exception as e:
            abort(500, message=f'new error {e}')


