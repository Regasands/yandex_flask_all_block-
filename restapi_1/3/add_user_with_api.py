from datetime import datetime
import random
from flask import request
import requests

# Списки для генерации случайных данных
surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Васильев", "Попов", "Новиков", "Федоров", "Морозов"]
names = ["Алексей", "Дмитрий", "Сергей", "Андрей", "Максим", "Иван", "Артем", "Никита", "Егор", "Павел"]
cities = {
    "Москва": "55.7558 37.6173",
    "Санкт-Петербург": "59.9343 30.3351",
    "Новосибирск": "55.0084 82.9357",
    "Екатеринбург": "56.8389 60.6057",
    "Казань": "55.7963 49.1088",
    "Нижний Новгород": "56.2965 43.9361",
    "Челябинск": "55.1644 61.4368",
    "Самара": "53.1959 50.1002",
    "Омск": "54.9884 73.3242",
    "Ростов-на-Дону": "47.2225 39.7187"
}

users = []

for i in range(10):
    city = random.choice(list(cities.keys()))
    city_coords = cities[city]
    
    user = {
        "surname": random.choice(surnames),
        "name": random.choice(names),
        "age": random.randint(18, 65),
        "position": f"Должность {random.randint(1, 10)}",
        "speciality": f"Специальность {random.randint(1, 10)}",
        "address": f"ул. {random.choice(['Ленина', 'Пушкина', 'Гагарина', 'Советская', 'Мира'])}, {random.randint(1, 100)}",
        "email": f"user{i+1}@example.com",
        "hashed_password": f"hashed_password_{i+1}",
        "modified_date": datetime.now().isoformat(),
        "city_form": city,
        "city_kord": city_coords  # Координаты в формате "широта долгота"
    }
    responce = requests.post('http://127.0.0.1:8080/add_user', json=user)
    print(responce.json())
    
