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
    likes = me.IntField(default=0)
    about_me = me.StringField()

    def __str__(self):
        return f"login: {self.login} | password: {self.password}"

class User(me.Document):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    age = me.IntField()
    interests = me.ListField(default=[])
    user_profile = me.ReferenceField(UserProfile, required=True)


user_profiles_list = [
    {"login": "lol",
     "password": "123",
     "about_me": "some lol",
     "likes": 3},
    {"login": "kek",
     "password": "1234",
     "about_me": "some kek",
     "likes": 5},
    {"login": "cheburek",
     "password": "12345",
     "about_me": "some cheburek",
     "likes": 6},
    {"login": "some_user",
     "password": "1234567",
     "about_me": "some some_user",
     "likes": 0}
]


user_data_list = [
    {"first_name": "Nikolai",
     "last_name": "Sviridov",
     "interests": ["mma", "programming", "blogging"],
     "age": 29
     },
    {"first_name": "Anna",
     "last_name": "Prozorova",
     "interests": ["smimming", "dancing", "singing"],
     "age": 35
     },
    {"first_name": "Semen",
     "last_name": "Ivanov",
     "interests": ["fishing", "riding"],
     "age": 21
     },
    {"first_name": "Chubaka",
     "last_name": "Chubakov",
     "interests": ["barking"],
     "age": 99
     }
]

# UserProfile.objects.all().delete()
# User.objects.all().delete()

user = User.objects.get(id='60c8617c088d7edb0941888e')
print(user)
user.interests = ['fghh']
user.save()

# for user_profile_data in zip(user_profiles_list, user_data_list):
#     print(user_profile_data)
#     from time import sleep
#     sleep(.5)
#     user_profile = UserProfile(**user_profile_data[0]).save()
#     user = User(user_profile=user_profile, **user_profile_data[1]).save()


# first_profile = UserProfile(login='Andrii', password='123')
# second_profile = UserProfile(login='Vasia', password='345')
# third_profile = UserProfile(login='Petia', password='987')
# first_profile.save()
# second_profile.save()
# third_profile.save()

# res = UserProfile.objects.all()
# for item in res:
#     print(item)
#     js_data = item.to_json()
#     print(js_data, type(js_data))
#     dict_data = json.loads(item.to_json())
#     print(dict_data, type(dict_data))

# UserProfile.objects(pk='60c7681ac28c04a1d011ba17').delete()

# UserProfile.objects.get(login="Andrii")
# res = UserProfile.objects.get(pk="60c766512efb3b840575959f")
# print(res)