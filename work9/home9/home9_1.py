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


me.connect("LESSON")


class UserProfile(me.Document):
    login = me.StringField(required=True)
    password = me.StringField(required=True)
    like = me.IntField(default=0)

    def __str__(self):
        return f"login: {self.login} | password: {self.password}"


# first_profile = UserProfile(login='Andrii', password='123')
# first_profile = UserProfile(login='sdfsd', password='sdf435')
first_profile = UserProfile(login='dsfdsfsdfs', password='123555')
first_profile.save()

# res = UserProfile.objects.all()
# for item in res:
#     print(item)
#     js_data = item.to_json()
#     print(js_data, type(js_data))
#     dict_data = json.loads(item.to_json())
#     print(dict_data, type(dict_data))

res = UserProfile.objects.get(pk="60c766512efb3b840575959f")
print(res)