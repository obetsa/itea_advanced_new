"""Перевести все существующие модели (Заявки, Департаменты, Сотрудники) на Flask-SQLAlchemy.
Перевести все ручки Flask-приложения из прошлого ДЗ на использование этих моделей.
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask import Flask, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

import psycopg2
from psycopg2 import sql

DB_URL = "postgresql://postgres:12345678@localhost:5432/postgres"
# order_service_db
# connect = psycopg2.connect(DB_URL)

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)
# db.create_all()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# SELECT_QUERY_departments = """SELECT * FROM order_service_db.departments"""


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


# def select_data():
#     with connect, connect.cursor() as cursor:
#         cursor.execute(SELECT_QUERY_departments)
#         result = cursor.fetchall()
#         for r in result:
#             print(r[0])


@app.route('/')
def index():
    return render_template("index.html")


def dep_get_dict(d):
    return {"Name": d.department_name, "Id": d.department_id, "Create date": str(d.create_dt)}


@app.route("/departments/all", methods=["POST", "GET"])
def dep_get_data():
    return render_template('department.html', lst=[dep_get_dict(i) for i in Departments.query.all()])


@app.route("/create_departments", methods=["POST"])
def create_departments():
    if request.method == 'POST':
        departments_data = json.loads(request.data)
        department_profile = Departments(department_name=departments_data["department_name"])
        db.session.add(department_profile)
        db.session.flush()
        db.session.commit()
        return render_template("departments.html", departments_data=departments_data)
    elif request.method == "GET":
        return Response("Ничего не найдено", status=404)


@app.route('/search_department_by_id/<string:search_by_id>', methods=['GET'])
def search_department_by_id(search_by_id):
    search_departments = Departments.query.filter_by(department_id=search_by_id).first()
    return render_template("departments.html", search_departments=search_departments)


@app.route('/delete_department_id/<string:delete_by_id>', methods=['DELETE'])
def delete_department_id(delete_by_id):
    delete_id = Departments.query.filter_by(department_id=delete_by_id).first()
    db.session.delete(delete_id)
    db.session.commit()
    return f'OK, department: {delete_id} deleted'


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
        return render_template("employees.html", employees_data=employees_data)
    elif request.method == "GET":
        return Response("Ничего не найдено", status=404)


@app.route('/search_employees_by_id/<string:search_by_id>', methods=['GET'])
def search_employees_by_id(search_by_id):
    search_employees = Employees.query.filter_by(employees_id=search_by_id).first()
    return render_template("employees.html", search_employees=search_employees)


@app.route('/delete_employees_id/<string:delete_by_id>', methods=['DELETE'])
def delete_employees_id(delete_by_id):
    delete_id = Employees.query.filter_by(employee_id=delete_by_id).first()
    db.session.delete(delete_id)
    db.session.commit()
    return f'OK, employees: {delete_id} deleted'


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
        return render_template("orders.html", order_data=order_data)
    elif request.method == "GET":
        return Response("Ничего не найдено", status=404)


@app.route('/search_order_by_id/<string:search_by_id>', methods=['GET'])
def search_order_by_id(search_by_id):
    search_order = Orders.query.filter_by(order_id=search_by_id).first()
    return render_template("orders.html", search_order=search_order)


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

# select_data()


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()

# python home14_1.py db init
# python home14_1.py db migrate
# python home14_1.py db upgrade
