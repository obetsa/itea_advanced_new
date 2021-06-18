"""Продолжаем работу над нашей CRM. Теперь нужно реализовать несколько web-ручек для управления нашей системой:
создание департамента, заявки, сотрудника
редактирование информации о департаменте, заявке сотруднике
удаление данных о заявке, департаменте и сотруднике
поиск по id/дате/любому другому параметру (на ваш выбор) департамента, сотрудника, зявки


Для выполнения ДЗ можно использовать интеграцию с любой изученной БД (sqlite, Postgresql, Mongo)"""

from flask import Flask, request
from datetime import datetime
import mongoengine as me

me.connect("home9")

app = Flask(__name__)


@app.route('/')
def hello():
    return f"{datetime.now()}"

if __name__ == "__main__":
    app.run(debug=True)