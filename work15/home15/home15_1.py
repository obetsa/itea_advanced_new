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
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))


class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_dt = db.Column(db.DateTime)
    c_name = db.Column(db.String(50))
    chat_id = db.Column(db.Integer)
    password = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(20))
    is_subscribed = db.Column(db.Boolean, default=False)


class NotificationTasks(db.Model):
    notification_task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_dt = db.Column(db.DateTime, default=datetime.now())
    message = db.Column(db.String(100))
    name = db.Column(db.Integer)
    profile_tg_chat_id = db.Column(db.String(10), nullable=True)


@app.route("/create_departments", methods=["POST"])
def create_departments():
    if request.method == 'POST':
        departments_data = json.loads(request.data)
        department_profile = Departments(department_name=departments_data["department_name"])
        db.session.add(department_profile)
        db.session.flush()
        db.session.commit()
        return 'OK'


@app.route('/search_department_by_id/<string:search_by_id>', methods=['GET'])
def search_department_by_id(search_by_id):
    search_departments = Departments.query.filter_by(department_id=search_by_id).first()
    return f'OK: {search_departments}'


@app.route('/delete_department_id/<string:delete_by_id>', methods=['DELETE'])
def delete_department_id(delete_by_id):
    delete_id = Departments.query.filter_by(department_id=delete_by_id).first()
    db.session.delete(delete_id)
    db.session.commit()
    return f'OK, department: {delete_by_id} deleted'


@app.route('/create_employee', methods=["POST", "GET"])
def create_employee():
    if request.method == 'POST':
        employees_data = json.loads(request.data)
        employee_profile = Employees(employee_id=employees_data['employee_id'],
                                     fio=employees_data['fio'],
                                     position=employees_data['position'],
                                     department_id=employees_data['department_id'])
        db.session.add(employee_profile)
        db.session.flush()
        db.session.commit()
        return 'OK'


@app.route('/search_employees_by_id/<string:search_by_id>', methods=['GET'])
def search_employees_by_id(search_by_id):
    search_employees = Employees.query.filter_by(employees_id=search_by_id).first()
    return f'OK: {search_employees}'


@app.route('/delete_employees_id/<string:delete_by_id>', methods=['DELETE'])
def delete_employees_id(delete_by_id):
    delete_id = Employees.query.filter_by(employee_id=delete_by_id).first()
    db.session.delete(delete_id)
    db.session.commit()
    return f'OK, employees: {delete_by_id} deleted'


@app.route('/create_order', methods=["POST", "GET"])
def create_order():
    if request.method == 'POST':
        order_data = json.loads(request.data)
        order_profile = Orders(create_dt=order_data['create_dt'],
                               order_type=order_data['order_type'],
                               description=order_data['description'],
                               status=order_data['status'],
                               serial_no=order_data['serial_no'],
                               creator_id=order_data['creator_id'],
                               )
        db.session.add(order_profile)
        db.session.flush()
        db.session.commit()
        return 'OK'


@app.route('/search_order_by_id/<string:search_by_id>', methods=['GET'])
def search_order_by_id(search_by_id):
    search_order = Orders.query.filter_by(order_id=search_by_id).first()
    return f'OK: {search_order}'


@app.route('/change_order_status', methods=['PATCH'])
def change_order_status():
    if request.method == 'PATCH':
        order_status = json.loads(request.data)
        get_id = Orders.query.filter_by(order_id=order_status['order_id']).first()
        get_id.status = order_status['Closed']
        get_id.update_dt = datetime.now()
        db.session.commit()
        return f'OK: Status changed'


@app.route('/delete_order_id/<string:delete_by_id>', methods=['DELETE'])
def delete_order_id(delete_by_id):
    delete_id = Orders.query.filter_by(order_id=delete_by_id).first()
    db.session.delete(delete_id)
    db.session.commit()
    return f'OK, order: {delete_by_id} deleted'


if __name__ == '__main__':
    # app.run(debug=True)

    manager.run()
