""" 1. Реализуйте базовый класс Car.
У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Реализовать метод для user-friendly вывода информации об автомобиле. """

class Car:

    def __init__(self, speed, colour, name, speed_limit, is_police=False):
        self.speed = int(speed)
        self.colour = colour
        self.name = name
        self.is_police = is_police
        self.speed_limit = int(speed_limit)
    
    def show_speed(self):
        print(self.speed)
    
    def go(self):
        print("...-o--o-")

    def stop(self):
        print("-o--o-")

    def turn(self, direction):
        print(f'turn to {direction}')

    def accelerate(self):
        self.speed += 10

    def __str__(self):
        return f"Car {self.name}, {self.colour} colour has {self.speed} speed {'police' if self.is_police else ''}"

    def show_speed(self):
        if self.speed >= self.speed_limit:
            print("too big")

    def show_speed(self):
        if self.speed >= self.speed_limit:
            print("too big")

class TownCar(Car):
    def __init__(self, *args, speed_limit=60):
        super().__init__(*args, speed_limit)


class WorkCar(Car):
    def __init__(self, *args, speed_limit=40):
        super().__init__(*args, speed_limit)

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, *args, is_police=True):
        super().__init__(*args, is_police)
    

tachka = Car("180", "red", "BMW", "10")
tachka_1 = TownCar("50", "black", "Volvo")
# tachka_2 = WorkCar("50", "silver", "Audi")
# tachka_3 = PoliceCar("50", "silver", "Lada")
tachka.go()
tachka.turn("right")
print(tachka_1.show_speed)
print(tachka.name)
print(tachka.speed)
tachka.accelerate()
print(tachka.speed)
tachka.stop()
tachka.show_speed()
tachka_1.show_speed()
tachka_1.accelerate()
tachka_1.show_speed()
# tachka_2.show_speed()
# tachka_3.show_speed()
print(tachka)
print(tachka_1)
# print(tachka_2)
# print(tachka_3)
