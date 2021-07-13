"""
1. (ПИШЕМ КАСТОМНЫЕ КЛАССЫ) На основе прошлых ДЗ необходимо создать модели представлений для классов
ДЕПАРТАМЕНТЫ (Departments), СОТРУДНИКИ (Employees), ЗАЯВКИ (Orders). Реализовать магические методы вывода
информации на экран как для пользователя, так и для "машинного" отображения.
Предусмотреть все необходимые ограничения и связи моделей между собой (*).
У каждой модели предусмотрите метод, который бы мог осуществлять запись хранимой в экземпляре информации в отдельный
json-файл с именем вида <id записи>.json. Если id не существует - выдавать ошибку.

2. Преобразовать все самописные классы-модели из прошлых ДЗ (из задачи 1: Заявки - Orders, Департаменты - Departments,
Сотрудники - Employees) в модели для использования в MongoDB. Предусмотреть необходимые связи, валидацию
данных и ограничения.
Написать функции, которые будут:
создавать/изменять/удалять новую заявку/сотрудника/департамент
Подсказка: у вас должно получиться 3 модели и 9 функций =)
"""

import mongoengine as me
import json
from datetime import datetime as dt

me.connect("home9")

department = [
    {"department_name": "IT1"},
    {"department_name": "IT2"},
    {"department_name": "IT1"},
    {"department_name": "IT3"},
    {"department_name": "IT1"},
    {"department_name": "IT3"},
    {"department_name": "IT2"}
]

employees = [
    {"fio": "Andrii",
     "position": "chef"
     },
    {"fio": "Nikolai",
     "position": "zam"
     },
    {"fio": "Vasia",
     "position": "worker"
     },
    {"fio": "Igor",
     "position": "svarchik"
     },
    {"fio": "Sasha",
     "position": "komputorshchik"
     },
    {"fio": "Jenia",
     "position": "gamer"
     },
    {"fio": "Dmitriy",
     "position": "proffesor"
     },
]

orders = [
    {"created_dt": '2021-01-07',
     "order_type": "order_type_1",
     "description": "some",
     "status": "Active",
     "serial_no": 11111
     },
    {"created_dt": '2021-01-07',
     "order_type": "order_type_2",
     "description": "some",
     "status": "Active",
     "serial_no": 22222
     },
    {"created_dt": '2021-01-07',
     "order_type": "order_type_3",
     "description": "some",
     "status": "Active",
     "serial_no": 33333
     },
    {"created_dt": '2021-01-07',
     "order_type": "order_type_4",
     "description": "some",
     "status": "Active",
     "serial_no": 44444
     },
    {"created_dt": '2021-01-07',
     "order_type": "order_type_5",
     "description": "some",
     "status": "Closed",
     "serial_no": 55555
     }
]


class Department(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField(default=None)
    department_name = me.StringField(required=True)

    def __str__(self):
        return f"department_name: {self.department_name}"

    def __repr__(self):
        return f"Машинный вывод информации: department_name: {self.department_name}"

    def save(self, *args, **kwargs):
        self.created_dt = dt.now()
        return super().save(*args, **kwargs)


class Employees(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField(default=None)
    fio = me.StringField(required=True)
    position = me.StringField(required=True)
    department_id = me.ReferenceField(Department, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"fio: {self.fio} | position: {self.position}"

    def __repr__(self):
        return f"Машинный вывод информации: fio: {self.fio} | position: {self.position}"

    def save(self, *args, **kwargs):
        self.created_dt = dt.now()
        return super().save(*args, **kwargs)


class Orders(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField(default=None)
    order_type = me.StringField(required=True)
    description = me.StringField()
    status = me.StringField(required=True)
    serial_no = me.IntField(default=0)
    creator_id = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"created_dt: {self.created_dt} | order_type: {self.order_type} | description: {self.description} | " \
               f"status: {self.status} | serial_no: {self.serial_no} | creator_id: {self.creator_id}"

    def __repr__(self):
        return f"Машинный вывод информации: created_dt: {self.created_dt} | order_type: {self.order_type} | " \
               f"description: {self.description} | " f"status: {self.status} | serial_no: {self.serial_no} | " \
               f"creator_id: {self.creator_id}"

    def save(self, *args, **kwargs):
        self.created_dt = dt.now()
        return super().save(*args, **kwargs)


"""Создания:"""

for user_profile_data in zip(department, employees):
    print(user_profile_data)
    department_id = Department(**user_profile_data[0]).save()
    user = Employees(department_id=department_id, **user_profile_data[1]).save()

for orders_data in zip(employees, orders):
    print(orders_data)
    creator_id = Employees(**orders_data[0]).save()
    order = Orders(creator_id=creator_id, **orders_data[1]).save()

"""Написать функции, которые будут:
создавать/изменять/удалять новую заявку/сотрудника/департамент"""
# department


def create_dep():
    Department(department_name='IT16').save()


def update_dep():
    dep = Department.objects(department_name='IT15')
    dep.update(department_name='IT13')


def delete_dep():
    Department.objects.all().delete()


# employees


def create_empl():
    Department(fio='Andrii', position='chef').save()


def update_empl():
    empl = Employees.objects(fio='Andrii', position='chef')
    empl.update(position='boss')


def delete_empl():
    Employees.objects.all().delete()


# orders


def create_orders():
    Orders(order_type='order_type2', description='some', status='Active', serial_no='77777',
           creator_id='60d45cf006e8462e16157ad2').save()


def update_orders():
    orde = Orders.objects(order_type='order_type2')
    orde.update(order_type='order_type3')


def delete_orders():
    Orders.objects.all().delete()


"""All in json"""


def employee_json():
    data_from_mong_employee = Employees.objects()
    for obj in data_from_mong_employee:
        print(obj)
        js_data = obj.to_json()
        print(type(js_data), js_data)


def department_json():
    data_from_mong_department = Department.objects()
    for obj in data_from_mong_department:
        print(obj)
        js_data = obj.to_json()
        print(type(js_data), js_data)


def orders_json():
    data_from_mong_orders = Orders.objects()
    for obj in data_from_mong_orders:
        print(obj)
        js_data = obj.to_json()
        print(type(js_data), js_data)


"""Id employee in json"""


def json_id_employee(id_e):
    res = Employees.objects.get(pk=id_e)
    res_json = json.loads(res.to_json())
    with open(f"{id}.json", "w") as json_f:
        json.dump(res_json, json_f)


def json_id_department(id_e):
    res = Department.objects.get(pk=id_e)
    res_json = json.loads(res.to_json())
    with open(f"{id}.json", "w") as json_f:
        json.dump(res_json, json_f)


def json_id_orders(id_o):
    res = Orders.objects.get(pk=id_o)
    res_json = json.loads(res.to_json())
    with open(f"{id}.json", "w") as json_f:
        json.dump(res_json, json_f)
