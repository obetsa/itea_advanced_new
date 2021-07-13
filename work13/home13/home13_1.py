"""
Сделать шаблоны для отображения сотрудников, заявок и департаментов и прикрутить их к соответствующим flask-методам.
Используйте 1 базовый шаблон, от которого унаследуйте все остальные. Что хотелось бы видеть:
 - навигационную панель (можно взять из классной работы или написать свою собственную)
 - удобный вывод информации (ограничение по количеству записей, выводимых на экран и использование
 списка с точками или цифрами при выводе)
"""

from flask import Flask, render_template
import psycopg2
from psycopg2 import sql
from datetime import datetime as dt

DB_URL = "postgres://postgres:12345678@localhost:5432/postgres"
connect = psycopg2.connect(DB_URL)

app = Flask(__name__)

SELECT_QUERY = sql.SQL('''SELECT * FROM order_service_db.departments, order_service_db.employees, 
order_service_db.orders ''')


class Departments:
    # SELECT_QUERY_departments = """SELECT * FROM order_service_db.departments"""
    SHOW_DEPARTMENT_QUERY = sql.SQL('''SELECT department_id, department_name FROM order_service_db.departments ''')

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id


class Employees:
    # SELECT_QUERY_employees = """SELECT * FROM order_service_db.employees"""
    SHOW_EMPLOYEES_QUERY = sql.SQL('''SELECT employee_id, fio, position, 
                                    department_id FROM order_service_db.employees ''')

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id


class Orders:
    # SELECT_QUERY_orders = """SELECT * FROM order_service_db.orders"""
    SHOW_ORDERS_QUERY = sql.SQL('''SELECT order_id, created_dt, order_type, description, 
            status, serial_no, creator_id FROM order_service_db.orders ''')

    def __init__(self, order_type, description, status, serial_no, creator_id, order_id=None):
        self.created_dt = str(dt.now())
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id
        self.order_id = order_id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all')
def all_data():
    with connect, connect.cursor() as cursor:
        cursor.execute(SELECT_QUERY, )
        res = cursor.fetchall()
    return render_template('all.html', result=res)


@app.route('/departments')
def departments():
    with connect, connect.cursor() as cursor:
        cursor.execute(Departments.SHOW_DEPARTMENT_QUERY, )
        res = cursor.fetchall()
    return render_template('departments.html', depp=res)


@app.route('/employees')
def employees():
    with connect, connect.cursor() as cursor:
        cursor.execute(Employees.SHOW_EMPLOYEES_QUERY, )
        res = cursor.fetchall()
    return render_template('employees.html', empl=res)


@app.route('/orders')
def orders():
    with connect, connect.cursor() as cursor:
        cursor.execute(Orders.SHOW_ORDERS_QUERY, )
        res = cursor.fetchall()
    return render_template('orders.html', orde=res)


if __name__ == "__main__":
    app.run(debug=True)
