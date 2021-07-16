"""1. Создать Телеграм-бота. Создать таблицу, в которую при обращении к Телеграм-боту будет сохраняться следующая
информация:
- nickname пользователя;
- идентификатор чата, через которое происходит общение;
- дата и время получения сообщения

2. Создать новую модель "Клиенты" (Customers), в которой предусмотреть на своё усмотрение необходимые поля, ограничения
и связи. Обязательным будет наличие в вашей модели поля is_subscribed (для подписки на уведомления).

Данная модель будет ответственна за работу с информацией о пользователях, которые оставляют заявки на консультацию
или ремонт. Подумайте над тем, какие дополнения потребует ваша модель Orders и внесите их.
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from typing import Callable

DB_URL = "postgresql://postgres:12345678@localhost:5432/order_service_db"

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Departments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(75), unique=True)


class Employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(50), nullable=False, unique=True)
    position = db.Column(db.String(75))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_dt = db.Column(db.DateTime, default=datetime.now())
    update_dt = db.Column(db.DateTime, nullable=True)
    order_type = db.Column(db.String(25), nullable=False)
    descriptions = db.Column(db.String(200))
    status = db.Column(db.String(10), nullable=False)
    serial_no = db.Column(db.Integer, nullable=False, unique=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)


class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_dt = db.Column(db.DateTime)
    name = db.Column(db.String(50))
    password = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(20))
    is_subscribed = db.Column(db.Boolean, default=False)


if __name__ == '__main__':
    # app.run(debug=True)

    manager.run()
