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
import json
import psycopg2
from psycopg2 import sql
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Process


DB_URL = "postgres://postgres:12345678@localhost:5432/postgres"
connect = psycopg2.connect(DB_URL)


class Employees:
    SEARCH_EMPLOYEES_ID = sql.SQL("""SELECT employee_id, fio, position, department_id FROM order_service_db.employees 
                                WHERE creator_id = %s""")

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id

    @staticmethod
    def get_data_by_id(id_):
        with connect, connect.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM order_service_db.employees where employee_id={id_}""")
            return {"Employees": cursor.fetchall()}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/employees/<string:id_list>", methods=['GET'])
def get_data_by_id(id_list):
    data = dict()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [pool.submit(get_data, i) for i in id_list.split()]
    for future in as_completed(results):
        data[f"Id:{future.result()[0]}"] = future.result()
    save_in_json(data)
    return data


def save_in_json(data):
    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def get_data(id_):
    return Employees.get_data_by_id(id_)["Employees"][0]


# @app.route('/get_emloyees', methods=['GET'])
# def get_emloyees():
#     p = Process(target=get_emloyees)
#     p.start()
#     data_employees = {}
#     employees_id = json.loads(request.data)
#     print("id: ", employees_id)
#     with connect, connect.cursor() as cursor:
#         for key in employees_id:
#             cursor.execute(Employees.SEARCH_EMPLOYEES_ID, (employees_id[key],))
#             res = cursor.fetchall()
#             data_employees[employees_id[key]] = list(res[0])
#         return json.dumps(data_employees)
#     p.join()


if __name__ == "__main__":
    app.run(debug=True)
