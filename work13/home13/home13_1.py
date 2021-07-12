"""
Сделать шаблоны для отображения сотрудников, заявок и департаментов и прикрутить их к соответствующим flask-методам.
Используйте 1 базовый шаблон, от которого унаследуйте все остальные. Что хотелось бы видеть:
 - навигационную панель (можно взять из классной работы или написать свою собственную)
 - удобный вывод информации (ограничение по количеству записей, выводимых на экран и использование
 списка с точками или цифрами при выводе)
"""

from flask import Flask, render_template, url_for
import psycopg2
from psycopg2 import sql
from datetime import datetime as dt

DB_URL = "postgres://postgres:12345678@localhost:5432/postgres"
connect = psycopg2.connect(DB_URL)

app = Flask(__name__)

class Departments:
    SHOW_DEPARTMENT_QUERY = sql.SQL('''SELECT department_id, department_name FROM departments ''')

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/departments')
def departments():
    with connect, connect.cursor() as cursor:
        cursor.execute(Departments.SHOW_DEPARTMENT_QUERY, )
        res = cursor.fetchall()
    return render_template('index.html', depp=res)


if __name__ == "__main__":
    app.run(debug=True)