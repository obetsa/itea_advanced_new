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

conn = psycopg2.connect("postgres://postgres:12345678@localhost:5432/postgres")

CREATE_QUERY = sql.SQL(
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
	department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL
    );
""")

departments = [["IT"], ["IT_2"]]

employees = [("Andrii", "chef", 3),
             ("Vasia", "worker", 3),
             ("Vanya", "gamer", 2),
             ("Sasha", "programist", 2)]

orders = [(datetime.now(), 'order_type_1', 'Active', 11111, 2),
          (datetime.now(), 'order_type_2', 'Active', 22222, 2),
          (datetime.now(), 'order_type_3', 'Active', 33333, 3),
          (datetime.now(), 'order_type_4', 'Active', 44444, 4),
          (datetime.now(), 'order_type_5', 'Active', 55555, 5),
          (datetime.now(), 'order_type_6', 'Closed', 66666, 5),
          (datetime.now(), 'order_type_7', 'Closed', 77777, 3)]


INSERT_QUERY_departments = sql.SQL("""INSERT INTO order_service_db.departments (department_name) 
                                        VALUES (%s)""")
INSERT_QUERY_employees = sql.SQL("""INSERT INTO order_service_db.employees (fio, position, department_id) 
                            VALUES (%s, %s, %s)""")
INSERT_QUERY_orders = sql.SQL("""INSERT INTO order_service_db.orders (created_dt, order_type, status, serial_no, 
                                creator_id) VALUES (%s, %s, %s, %s, %s)""")


SELECT_QUERY_departments = """SELECT * FROM order_service_db.departments"""
SELECT_QUERY_employees = """SELECT * FROM order_service_db.employees"""
SELECT_QUERY_orders = """SELECT * FROM order_service_db.orders"""


def create_tables():
    with conn, conn.cursor() as cursor:
        cursor.execute(CREATE_QUERY)

def insert_data():
    with conn, conn.cursor() as cursor:
        for department in departments:
            cursor.execute(INSERT_QUERY_departments, department)

    with conn, conn.cursor() as cursor:
        for employee in employees:
            cursor.execute(INSERT_QUERY_employees, employee)

    with conn, conn.cursor() as cursor:
        for order in orders:
            cursor.execute(INSERT_QUERY_orders, order)

def select_data():
    with conn, conn.cursor() as cursor:
        cursor.execute(SELECT_QUERY_departments)
        result = cursor.fetchall()
        for r in result:
            print(r[0])
    with conn, conn.cursor() as cursor:
        cursor.execute(SELECT_QUERY_employees)

    with conn, conn.cursor() as cursor:
        cursor.execute(SELECT_QUERY_orders)


def main():
    # create_tables()
    # insert_data()
    select_data()

if __name__ == '__main__':
    main()


