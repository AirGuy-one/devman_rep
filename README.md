# Проект про интересные места в Москве, которые следует посетить
## Простая инструкция по запуску проекта локально:

1. Создайте нужные папки для сохранения json файлов командой
```sh
python3 manage.py add_folders
```
2. Создайте файл .env и запишите в него следующие переменные:
    * SECRET_KEY='' (С помощью этой переменной проект начинает работать)
    * DEBUG=True (С помощью этой переменной мы выбираем режим, в котором будем запускать проект)
3. Выполнить миграции командной
```sh
python3 manage.py migrate
```
4. Загрузить данные для бд через json файлы командой
```sh
python3 manage.py load_place <link to json file>
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

Ссылка на пример json файла: (https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)

Ссылка на демо-версию сайта: (https://airguy.pythonanywhere.com/)
