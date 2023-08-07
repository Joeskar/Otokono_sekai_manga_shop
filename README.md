<h2 align="center">Online Store</h2>

### Описание проекта:

Онлайн магазин c мангой

### Инструменты разработки

*Стек:*

- Python >= 3.10
- Django == 4.1.3
- PostgreSQL

## Разработка

##### 1) Поставить звездочку)

##### 2) Клонировать репозиторий

    git clone https://github.com/Joeskar/Otokono_sekai_manga_shop.git

##### 3) Создать виртуальное окружение

    cd config
    
    python -m venv venv

##### 4) Активировать виртуальное окружение

Linux

    source venv/bin/activate

Windows

    ./venv/Scripts/activate

##### 5) Устанавливить зависимости:

    pip install -r requirements.txt

##### 6) Запустить контейнер:

    docker-compose up

##### 7) Выполнить команду для выполнения миграций

    python manage.py migrate

##### 8) Создать суперпользователя

    python manage.py createsuperuser

##### 9) Запустить сервер

    python manage.py runserver

##### 10) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin

## License

Copyright (c) 2023-present, Joeskar - Social Askar

