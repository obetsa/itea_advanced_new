"""
1. Сделать шаблоны для отображения сотрудников, заявок и департаментов и прикрутить их к соответствующим методам.
Используйте 1 базовый шаблон, от которого унаследуете все остальные.

- Написать ручку на flask, которая будет принимать в теле запроса список id пользователей. (@app.route)
- Дальше по каждому id нужно ОТДЕЛЬНО сделать запрос в БД на получение информации о пользователе. (через модель,
но не прокидывать все id сразу! вытаскивайте по одному! то есть sql запрос должен быть не select * from users where
 user_id = any(1, 2, 3, 4), а чтобы он был select * from users where user_id = 1). Для mongoengine такие же ограничения
 на использование выборок с помощью моделей.
- Реализовать механизм сбора данных о пользователе через процессы или потоки (то есть нужно, чтобы были параллельные
запросы в БД)
- Получив информацию по каждому пользователю вернуть её в составе json-объекта в ответе (то есть в ответе должен быть
json)
"""

from flask import Flask, request, render_template
from h10 import *
import mongoengine as me
from datetime import datetime as dt

me.connect("home9")

app = Flask(__name__)

@app.route('/employees/<string:id>', methods=['GET'])
def get_id(id):
    user = Employees.objects(id=id)
    return f"{user}"



if __name__ == "__main__":
    app.run(debug=True)