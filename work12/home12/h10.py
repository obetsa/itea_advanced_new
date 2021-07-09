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
    created_dt = me.DateTimeField(required=None)
    updated_dt = me.DateTimeField(default=None)
    department_name = me.StringField(required=True)

    def __str__(self):
        return f"department_name: {self.department_name}"


class Employees(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField(default=None)
    fio = me.StringField(required=True)
    position = me.StringField(required=True)
    department_id = me.ReferenceField(Department, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"fio: {self.fio} | position: {self.position}"


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
