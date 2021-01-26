# api_final_yatube

Проект представляет собой API для проетка [hw05_final](https://sm-yamdb.tk/)

## Начало

Клонировать проект:
```
Git clone https://github.com/SergeyMMedvedev/api_final_yatube.git
```

### Установка

Перейти в корневую директорию проекта и активировать виртуальное окружение 
```
$ source venv/Scripts/activate
```

Установить requirements

```
$ pip install requirements.txt
```

Запуск сервера разработчика
 
```
$ python manage.py runserver
```

## Проверка работоспособности

Примеры запросов к api_final_yatube:

GET http://localhost:8000/api/v1/posts/

Response:
```
[
    {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
    }   
]
```
GET http://localhost:8000/api/v1/posts/{post_id}/comments/


```
[
    {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
    }
]
```
Полный список доступных запросов к приложению можно посмотреть:
* http://localhost:8000/redoc/

Для изменения содержания базы данных монжо воспользоваться админкой Django:
* http://localhost:8000/admin/


## Автор

* **Сергей Медведев** -  [SergeyMMedvedev](https://github.com/SergeyMMedvedev)
