
import requests
from pprint import pprint

BASE_URL = 'http://127.0.0.1:8080/api/v2/jobs'


def test_jobs_api():
    # Тест 1: Получение всех работ
    print('\n=== GET ALL JOBS ===')
    response = requests.get(BASE_URL)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 2: Получение одной работы (существующей)
    print('\n=== GET JOB 1 ===')
    response = requests.get(f'{BASE_URL}/2')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 3: Получение несуществующей работы
    print('\n=== GET NON-EXISTENT JOB ===')
    response = requests.get(f'{BASE_URL}/9999')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 4: Редактирование работы
    print('\n=== UPDATE JOB 2 ===')
    job_data = {
        'job': 'Обновление API',
        'work_size': 12,
        'team_leader': 2,
        'collaborators': ['2', '3'],
        'start_date': '2025-04-10',
        'end_date': '2025-04-12',
        'is_finished': True
    }
    response = requests.put(f'{BASE_URL}/2', json=job_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 5: Ошибка обновления (неверный ID)
    print('\n=== UPDATE NON-EXISTENT JOB ===')
    response = requests.put(f'{BASE_URL}/9999', json=job_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 6: Создание новой работы
    print('\n=== CREATE JOB ===')
    new_job_data = {
        'job': 'Новая задача',
        'work_size': 8,
        'team_leader': 2,
        'collaborators': ['4', '5'],
        'start_date': '2025-04-14',
        'end_date': '2025-04-16',
        'is_finished': False
    }
    response = requests.post(BASE_URL, json=new_job_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 7: Удаление работы
    print('\n=== DELETE JOB 2 ===')
    response = requests.delete(f'{BASE_URL}/2')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 8: Удаление несуществующей работы
    print('\n=== DELETE NON-EXISTENT JOB ===')
    response = requests.delete(f'{BASE_URL}/9999')
    print(f'Status: {response.status_code}')
    pprint(response.json())


if __name__ == '__main__':
    test_jobs_api()
