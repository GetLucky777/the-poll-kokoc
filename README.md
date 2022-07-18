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
Запустить проект:
```
python manage.py runserver

# Скриншоты проекта
![image](https://user-images.githubusercontent.com/90413693/179611551-8cb2a990-b98a-4db2-91cf-1c46b90806fe.png)
![image](https://user-images.githubusercontent.com/90413693/179611755-d5aad012-29d4-475a-8015-1249ff751a96.png)
![image](https://user-images.githubusercontent.com/90413693/179611819-fa53d5b2-ba59-4992-adba-3ec98ffb0303.png)
![image](https://user-images.githubusercontent.com/90413693/179611928-9d5bb2a7-4a38-4ad0-84ff-aad55e7d603d.png)
