# Проект про интересные места в Москве, которые следует посетить
## Простая инструкция по запуску проекта локально:

1. Создайте файл .env по следующему примеру:
```
SECRET_KEY='django-insecure--we4h56we4h54er4he4rhe4rth46e5r6'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1,airguy.pythonanywhere.com'
```
2. Установите зависимости
```sh
pip install -r requirements.txt
```
3. Выполнить миграции командной
```sh
python3 manage.py migrate
```
4. Загрузить данные для бд через json файлы командой(пример json файла внизу)\
   Ссылка на пример json файла: (https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)
```sh
python3 manage.py load_place <ссылка на json файл>
```
5. Загрузить статику командной
```sh
python3 manage.py collectstatic
```
6. Запустить сервер локально, выпонив команду
```sh
python3 manage.py runserver
```

## Чтобы загрузить данные через админку Django, необходимо:

1. Создать суперпользователя
```sh
python3 manage.py createsuperuser
```
2. Заполнить имя и пароль(email не обязателен)

3. Зайти админку Django, написав после основного адреса /admin и загрузить данные

Ссылка на демо-версию сайта: (https://airguy.pythonanywhere.com/)
