"""Продолжаем работу с таблицами из домашнего задания №5 и классом Заяка из домашнего задания №2:
Расширить поведение класса Заявка. Теперь заявка должна иметь следующие методы, которые будут взаимодействовать
с БД (получать данные, изменять данные, удалять данные и т.д.):
создание новой заявки;
изменение статуса;
изменение описания;
изменение id создателя;
При изменении данных заявки в БД необходимо изменять поле updated_dt.
Аналогичные классы создать для департаментов и сотрудников. Во время выполнения задания постарайтесь максимально
использовать концепции ООП (инкапсуляцию, наследование, полиморфизм).
"""

import psycopg2
from psycopg2 import sql
from datetime import datetime
from envparse import Env

from abc import ABC, abstractmethod

env = Env()
PASS = env.str("fsdf@rfd")
DB_URL = env.str("SOME_DB_URL", default="postgres://postgres:@localhost:5432/postgres")
connect = psycopg2.connect(DB_URL)

"""
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt,
    order_type TEXT NOT NULL,
    description TEXT,
    status text NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    foreign key (creator_id) references employees (employee_id)
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


class BaseModel(ABC):
    @abstractmethod
    def create_date(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_data(self, *args, **kwargs):
        pass

    @abstractmethod
    def status_change(self, *args, **kwargs):
        pass

    @abstractmethod
    def description_change(self, *args, **kwargs):
        pass

    @abstractmethod
    def department_name_change(self, *args, **kwargs):
        pass

    @abstractmethod
    def position_change(self, *args, **kwargs):
        pass

    def real_method(self):
        pass


class DataRequiredException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs


class Order(BaseModel):
    count_request = 0

    CREATE_ORDER_QUERY = sql.SQL("""INSERT INTO orders (created_dt, updated_dt, order_type, description, status,
                                    serial_no, creator_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING order_id""")
    DELETE_ORDER_QUERY = sql.SQL("""DELETE FROM orders WHERE order_id = %s""")
    CHANGE_ORDER_QUERY = sql.SQL("""UPDATE orders SET updated_dt = %s, status = %s WHERE order_id = %s""")

    def __init__(self, created_dt, updated_dt, order_type,description, status, serial_no, creator_id, order_id=None):
        Order.date_object = datetime.now().strptime("%d %B, %Y")
        self.created_dt = Order.date_object
        self.updated_dt = updated_dt
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id
        self.order_id = order_id
        Order.count_request += 1

    # создание новой заявки
    def create_date(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CREATE_ORDER_QUERY, (datetime.now(), self.order_type, self.description,
                                                               self.status, self.serial_no, self.creator_id))
            order_id = cursor.fetchone()[0]
            self.order_id = order_id
        return {"order_id": order_id}

    # удалять данные
    def delete_data(self):
        if not self.order_id:
            raise DataRequiredException(message="Enter order_id")
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.DELETE_ORDER_QUERY, (self.order_id, ))

    # изменение статуса
    def status_change(self, new_status):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_ORDER_QUERY, (new_status, datetime.now(), self.order_id, ))

    # изменение описания
    def description_change(self, new_description):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_ORDER_QUERY, (new_description, datetime.now(), self.order_id, ))

    # ?? изменение id создателя ??

class Departments(BaseModel):
    CREATE_DEPARTMENT_QUERY = sql.SQL("""INSERT INTO departments (department_name) VALUES (%s) 
                                        RETURNING department_id""")
    CHANGE_DEPARTMENT_QUERY = sql.SQL("""UPDATE departments SET department_name = %s WHERE department_id = %s""")

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id

    def create_date(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CREATE_DEPARTMENT_QUERY, (self.department_name, ))
            department_id = cursor.fetchone()[0]
            self.department_id = department_id
        return {"department_id": department_id}

    def department_name_change(self, new_department_name):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_DEPARTMENT_QUERY, (new_department_name, ))


class Employees(BaseModel):
    CREATE_EMPLOYEES_QUERY = sql.SQL("""INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s) 
                                        RETURNING employee_id""")
    CHANGE_EMPLOYEES_QUERY = sql.SQL("""UPDATE employees SET position = %s WHERE department_id = %s""")

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id

    def create_date(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CREATE_EMPLOYEES_QUERY, (self.fio, self.position, self.department_id))
            employee_id = cursor.fetchone()[0]
            self.employee_id = employee_id
        return {"employee_id": employee_id}

    def position_change(self, new_position):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_EMPLOYEES_QUERY, (new_position, ))
