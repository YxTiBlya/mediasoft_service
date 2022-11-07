## **Карасев Степан**

# Сервис принимает и отвечает на http запросы

### Запуск через Docker compose
1. Склонировать репозиторий.
2. В .env файле вставить пароль от postgres.
3. В консоли перейти в папку с проектом и выполнить команду docker-compose up.
4. После ожидания скачивания и запуска контейнеров можно отправлять запросы на http://127.0.0.1:5000/, можно использовать модуль requests python или делать это в браузере.

### Пути
* http://127.0.0.1:5000/city - получить json объект с городами
* http://127.0.0.1:5000/city/id/street - получить json объект с улицами определенного города (id брать из json объекта с городами)
* http://127.0.0.1:5000/shop - получить json объект со всеми магазинами (аргументы фильров: city, street - text; open - 0/1).
Так же на этот путь можно отправить post запрос с json объектом магазина чтобы сохранить его в бд (пример объекта ниже).

Пример json объекта:
```Python
{"name": "Пятерочка", "home": 23, "city": "Санкт-Петербург", "street": "Пушкинская", "openIn": "08:00", "closeIn": "23:00"}
```

Пример отправки post запроса на сервер:
```Python
import requests

param = {"name":"Пятерочка", "home":23,"city":"Санкт-Петербург", "street":"Пушкинская", "openIn":"08:00", "closeIn":"23:00"}
r = requests.post('http://127.0.0.1:5000/shop', json=param)
print(r.status_code)
print(r.json())
```
> С КЛАДР (ФИАС) не разобрался :(

### Языки и технологии
![Python](https://img.shields.io/badge/-Python-090909?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/-Flask-090909?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/-Docker-090909?style=for-the-badge&logo=Docker)
![Postgres](https://img.shields.io/badge/-Postgres-090909?style=for-the-badge&logo=Postgresql)
![Sql-alchemy](https://img.shields.io/badge/-SQLAlchemy-090909?style=for-the-badge&logo=)