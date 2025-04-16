
import requests
from pprint import pprint

BASE_URL = 'http://127.0.0.1:8080/api/v2/users'


def test_users_api():
    # Тест 1: Получение всех пользователей
    print('\n=== GET ALL USERS ===')
    response = requests.get(BASE_URL)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 2: Получение одного пользователя (существующего)
    print('\n=== GET USER 1 ===')
    response = requests.get(f'{BASE_URL}/1')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 3: Получение несуществующего пользователя
    print('\n=== GET NON-EXISTENT USER ===')
    response = requests.get(f'{BASE_URL}/9999')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 4: Редактирование пользователя
    print('\n=== UPDATE USER 1 ===')
    user_data = {
        'surname': 'Иванов',
        'name': 'Иван',
        'age': 30,
        'position': 'Разработчик',
        'speciality': 'Backend',
        'address': 'Москва',
        'email': 'ivanov@example.com',
        'hashed_password': 'securepassword'
    }
    response = requests.put(f'{BASE_URL}/1', json=user_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 5: Ошибка обновления (неверный ID)
    print('\n=== UPDATE NON-EXISTENT USER ===')
    response = requests.put(f'{BASE_URL}/9999', json=user_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 6: Удаление пользователя
    print('\n=== DELETE USER 1 ===')
    response = requests.delete(f'{BASE_URL}/1')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 7: Удаление несуществующего пользователя
    print('\n=== DELETE NON-EXISTENT USER ===')
    response = requests.delete(f'{BASE_URL}/9999')
    print(f'Status: {response.status_code}')
    pprint(response.json())


if __name__ == '__main__':
    test_users_api()
