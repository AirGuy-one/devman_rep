# Проект про интересные места в Москве, которые следует посетить

## Чтобы запустить сайт локально, нужно:

* Создайте нужные папки для сохранения json файлов командой `python3 manage.py add_folders`
* Создайте файл .env и запишите в него следующие переменные:
    * SECRET_KEY=''
    * DEBUG=False
* Выполнить миграции командной `python3 manage.py migrate`
* Загрузить данные для бд через json файлы командой `python3 manage.py load_place <link of json file>`
* Загрузить статику командной `python3 manage.py collectstatic`
* Запустить сервер локально, выпонив команду `python3 manage.py runserver`
* Загрузить данные об интересных местах в бд через админку Django, написав после основного url >/admin

Ссылка на пример json файла: [https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json]

