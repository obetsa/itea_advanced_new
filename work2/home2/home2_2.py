""" 2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.

Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
полем.
У заявки должны быть следующие методы:
- метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
- метод, изменяющий статус заявки
- метод, возвращающий id заявки """

import time
from datetime import datetime

class Request:
    
    count_request = 0

    def __init__(self, id, name, ser_number, status='active'):
        self.__id = id
        self.time = datetime.now()
        self.name = name
        self.ser_number = ser_number
        self.status = status
        Request.count_request += 1

    def status_change(self):
        pass

    def request_id(self):
        return self.__id

    def r_close(self):
        self.status = "closed"
    
    def r_open(self):
        self.status = "active"
    
    def __str__(self):
        pending = datetime.now() - self.time
        delta = divmod(pending.total_seconds(), 60)
        return f'pending time: {delta[0]} minutes and {delta[1]} seconds'

         
r = Request(id="1", name='Test', ser_number='222')
t = Request(id="2", name='Test2', ser_number='SB222')
time.sleep(2)
print(r.status)
print(r.request_id())
print(t.request_id())
print(r.time)
print(Request.count_request)
print(r)
r.r_close()
print(r.status)