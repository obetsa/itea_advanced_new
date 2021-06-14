"""2.   Создайте абстрактный класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс и т.д.). 
    В базовом классе определите абстрактные методы, общие для приведённых типов. 
    В классах-наследниках реализуйте их, а также добавьте уникальные для каждого
 типа оргтехники функциональные возможности.

 Также создайте класс «Склад», экземпляр которого будет способен принимать в себя объекты техники на хранение.
 Организуйте для него протокол итерации (чтобы объекты вашего склада можно было бы перебирать).
"""
from abc import ABC, abstractmethod
from uuid import uuid4


class BaseOrgtech(ABC):
    # def __init__(self):
    #     pass

    @abstractmethod
    def ping(self):
        print("ping: ")


class Printer(BaseOrgtech):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def ping(self):
        super().ping()
        print("Printer\n")


class Scanner(BaseOrgtech):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ping(self):
        super().ping()
        print("Scanner\n")


class Xerox(BaseOrgtech):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ping(self):
        super().ping()
        print("Xerox")


TYPES_MAPPING = {
    "printer": Printer,
    "scanner": Scanner,
    "xerox": Xerox
}

class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, type, *args, **kwargs):
        id = uuid4()
        class_of_tech = TYPES_MAPPING[type]
        item = class_of_tech(id, *args, **kwargs)
        self.items.append(item)
        print('item added to warehouse')



# p = Printer()
# p.ping()
# s = Scanner()
# s.ping()
# x = Xerox()
# x.ping()

a = Warehouse()
a.add_item("printer", " Canon MF240")
print(a)



