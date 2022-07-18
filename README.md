# the-poll-kokoc
Тестовое задание на Django для сервиса опросов.

# Описание проекта

Сервис предназначен для прохождения опросов пользователями. Реализована регистрация, сброс и смена пароля. Реализован профиль пользователя, магазин для траты
зарабатываемой валюты на цветовую дифференциацию, список пользователей.

# Используемые технологии
- Python 3.9.10
- Django 2.2.16

# Запуск проекта
Клонировать репозиторий, перейти в новую директорию:
```
git clone https://github.com/GetLucky777/the-poll-kokoc
```
Инициализировать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/Scripts/activate
```
Установить зависимости проекта:
```
pip install -r requirements.txt
```
Выполнить миграции, для этого перейти в директорию с файлом manage.py:
```
python manage.py migrate
```
Зарегистировать администратора для добавления опросов:
```
python manage.py createsuperuser
```
Запустить проект:
```
python manage.py runserver
```
# Скриншоты проекта
![image](https://user-images.githubusercontent.com/90413693/179612440-b0a7190d-5a7c-4d27-842f-fec9fb6edc24.png)
![image](https://user-images.githubusercontent.com/90413693/179612752-9790d998-0b24-48af-85f2-f618e87bf763.png)
![image](https://user-images.githubusercontent.com/90413693/179612486-99acc30d-cc52-473f-9bdd-be94712e1ea3.png)
![image](https://user-images.githubusercontent.com/90413693/179612521-53a92434-100c-42be-bacd-bc004134b5e6.png)
![image](https://user-images.githubusercontent.com/90413693/179612546-c82a2d02-a40e-4972-b2ef-7f23e4270101.png)
