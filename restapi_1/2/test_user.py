import datetime
import requests
from pprint import pprint

BASE_URL = 'http://127.0.0.1:8080/api/users'  # Базовый URL без слеша на конце
now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
def test_api():
    # Тест 1: Получение всех user
    print('\n=== GET ALL user ===')
    response = requests.get(BASE_URL)
    print(f'Status: {response.status_code}')
    pprint(response.json())


    # Тест 3: Получение одной user
    print('\n=== GET ONE JOB ===')
    response = requests.get(f'{BASE_URL}/1')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 4: Несуществующий ID
    print('\n=== WRONG ID ===')
    response = requests.get(f'{BASE_URL}/1290')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 5: Создание user
    print('\n=== CREATE USER ===')
    user_data = {
        "surname": "Иванов",
        "name": "Иван",
        "age": 30,
        "position": "Инженер",
        "speciality": "Разработчик ПО",
        "address": "ул. Пушкина, д. 10",
        "email": f"ivanov@example.com{now}", 
        "hashed_password": "hashed_secure_password_123",
        "modified_date": "2025-04-14"
    }
    # Да

    response = requests.post(BASE_URL, json=user_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # Тест 6: Создание с неправильным is_finished
    print('\n=== CREATE WITH WRONG is_finished ===')
    user_data = {
        "surname": "Иванов",
        "name": "Иван",
        "age": 30,
        "position": "Инженер",
        "speciality": "Разработчик ПО",
        "address": "ул. Пушкина, д. 10",
        "email":  f"ivanov@example.com{now}1",
        "hashed_password": "hashed_secure_password_123",
        "modified_date": "2025-04-14 909090"
    }


    response = requests.post(BASE_URL, json=user_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())

    print('\n EDIT CORRECT')
       # Тест 8 редакитирование  работы корректное
    user_data = {
        "surname": "Иванов",
        "name": "Иван",
        "age": 30,
        "position": "Инженер",
        "speciality": "Разработчик ПО",
        "address": "ул. Пушкина, д. 10",
        "email":  f"ivanov@example.com{now}2",
        "hashed_password": "hashed_secure_password_123",
        "modified_date": "2025-04-14"
    }
    response = requests.put(BASE_URL + '/1', json=user_data)
    print(response.text)
    print(f'Status: {response.status_code}')
    pprint(response.json())
    
    
    print('\n  NO EDIT CORRECT error data')
    # Тест 9 редакитирование  работы не корректное ошибка в запросе 
    user_data = {
        "surname": "Иванов",
        "name": "Иван",
        "age": 30,
        "position": "Инженер",
        "speciality": "Разработчик ПО",
        "address": "ул. Пушкина, д. 10",
        "email":  f"ivanov@example.com{now}3",
        "hashed_password": "hashed_secure_password_123",
        "modified_date": "2025-04-149090909090yh8u9 jio"
    }
    response = requests.put(BASE_URL + '/1', json=user_data)
    print(f'Status: {response.status_code}')
    pprint(response.json())



    print('\n  NO EDIT CORRECT error id')
    # Тест 10 редакитирование  работы  не корректное не верный id
    response = requests.put(BASE_URL + '/322323')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    # тест 11 удаление верноеное
    print('\n DELETE ')
    response = requests.delete(BASE_URL + '/8')
    print(f'Status: {response.status_code}')
    pprint(response.json())

    
    # тест 11 удаление  не верноеное ошибка в id 

    print('\n ERROR DELETE ')
    response = requests.delete(BASE_URL + '/88989898989')
    print(f'Status: {response.status_code}')
    pprint(response.json())



if __name__ == '__main__':
    test_api()
