"""
SQL 2 ЧАСТЬ
Продолжаем работу с таблицами из домашнего задания №5:
1. Создать тестовый набор данных по каждой из таблиц в модуле python (лучше всего использовать список списков или
список кортежей). Написать скрипт, который бы осуществлял подключение к существующей БД и последовательно запускал
сначала скрипты на создание таблиц (из прошлого ДЗ: departments, employees, orders), а затем последовательно загружал
туда данные.
2. По тестовым данным необходимо написать следующие запросы:
    - запрос для получения заявок в определённом статусе (можно выбрать любой) за конкретный день, созданных
    конкретным сотрудником;
    - запрос, возвращающий список сотрудников и департаментов, в которых они работают
    - запрос, позволяющий получить количество заявок в определенном статусе (можно выбрать любой) по дням;
"""

import psycopg2
from psycopg2 import sql
from datetime import datetime

conn = psycopg2.connect("postgres://postgres:********@localhost:5432/postgres")

"""
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt DATE NOT NULL,
    order_type TEXT NOT NULL,
    description TEXT,
    status text NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES employees (employee_id)
    );

CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY key,
    fio TEXT NOT NULL,
    position TEXT,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    );

CREATE TABLE IF NOT EXISTS departments (
	department_id SERIAL PRIMARY key,
    department_name TEXT NOT NULL
    );
"""

orders = [(datetime.now(), 'order_type_1', 'Active', 11111, 1),
          (datetime.now(), 'order_type_2', 'Active', 22222, 2),
          (datetime.now(), 'order_type_3', 'Active', 33333, 3),
          (datetime.now(), 'order_type_4', 'Active', 44444, 4),
          (datetime.now(), 'order_type_5', 'Active', 55555, 5),
          (datetime.now(), 'order_type_6', 'Closed', 66666, 6),
          (datetime.now(), 'order_type_7', 'Closed', 77777, 7)]

employees = [("aaa", "qwe", 1),
             ("bbb", "asd", 1),
             ("ccc", "zxc", 2),
             ("ddd", "qwe", 2),]

departments = ["IT",
               "IT_2"]


SELECT_QUERY_orders = """SELECT * FROM orders"""
SELECT_QUERY_employees = """SELECT * FROM employees"""
SELECT_QUERY_departments = """SELECT * FROM departments"""


INSERT_QUERY_orders = sql.SQL("""INSERT INTO orders (created_dt, order_type, status, serial_no, creator_id) 
                            VALUES (%s, %s, %s, %s, %s)""")
INSERT_QUERY_employees = sql.SQL("""INSERT INTO employees(fio, position_, department_id) 
                            VALUES (%s, %s, %s)""")
INSERT_QUERY_departments = sql.SQL("""INSERT INTO departments(department_name) 
                            VALUES (%s)""")

with conn, conn.cursor() as cursor:
    for order in orders:
        cursor.execute(INSERT_QUERY_orders, order)

with conn, conn.cursor() as cursor:
    for employee in employees:
        cursor.execute(INSERT_QUERY_employees, employee)

with conn, conn.cursor() as cursor:
    for department in departments:
        cursor.execute(INSERT_QUERY_departments, department)





