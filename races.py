# В городе Тарантасске проходят гонки без ограничений.
# Это значит, что одновременно соревноваться могут гонщики на автомобилях,
# мотоциклах и даже гужевых повозках. Скорости автомобиля и мотоцикла зависят от того,
# каким бензином они заправлены - 98 позволяет ехать с полной скоростью,
# 95 уменьшает скорость на 10% для машин и на 20% для мотоциклов,
# 92-й - на 20% и 40% соответственно. Гужевые повозки едут с постояной скоростью.
# Длина кольцевой трассы равна M.
# Определить, какое транспортное средство будет ближе к финишу спустя время t после начала гонок
# (возможно, проходя при этом не первый круг). Если несколько средств будут одинаково близки,
# вывести нужно то, у которого меньше номер. Для описания транспортных средств используйте наследование классов.
#
# Формат ввода
# Программа получает на вход строку
# с натуральными числами N, M и t - количеством транспортных средств,
# длиной трассы и временем гонки соответственно.
# Дальше следуют N строк.
# В каждой записано три натуральных числа - индивидуальный номер транспортного средства,
# тип средства (1 - автомобиль, 2 - мотоцикл, 3 - гужевая повозка) и скорость данного средства.
# Если это автомобиль или мотоцикл, то в строке также есть четвёртое число - марка бензина,
# которым заправлено средство.
#
# Формат вывода
# Программа должна вывести одно число - номер транспортного средства,
# которое спустя время t окажется ближе всего к финишу.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, num, speed):
        self.position = 0
        self.num = num
        self.speed = speed

    @abstractmethod
    def move(self, time):
        pass


class Car(Vehicle):

    penalties = {
        98: 1,
        95: 0.9,
        92: 0.8,
    }

    def __init__(self, num, speed, fuel_type):
        super(Car, self).__init__(num, speed)
        self.penalty = self.penalties[fuel_type]

    def move(self, time):
        self.position = self.speed * self.penalty * time


class Motorcycle(Vehicle):

    penalties = {
        98: 1,
        95: 0.8,
        92: 0.6,
    }

    def __init__(self, num, speed, fuel_type):
        super(Motorcycle, self).__init__(num, speed)
        self.penalty = self.penalties[fuel_type]

    def move(self, time):
        self.position = self.speed * self.penalty * time


class Carriage(Vehicle):
    def move(self, time):
        self.position = self.speed * time


class Race:

    vehicle_types = {
        1: Car,
        2: Motorcycle,
        3: Carriage
    }

    def __init__(self):
        self.path_length = 0
        self.time = 0
        self.vehicles = []
        self._parse_input()

    def _parse_line(self, input_str):
        return list(map(int, input_str.split()))

    def _parse_input(self):
        num_vehicles, self.path_length, self.time = self._parse_line(input())
        for i in range(num_vehicles):
            parsed = self._parse_line(input())
            if len(parsed) == 4:
                vehicle_num, vehicle_type, speed, fuel_type = parsed
                self.vehicles.append(self.vehicle_types[vehicle_type](vehicle_num, speed, fuel_type))
            elif len(parsed) == 3:
                vehicle_num, vehicle_type, speed = parsed
                self.vehicles.append(self.vehicle_types[vehicle_type](vehicle_num, speed))
            else:
                raise Exception("Invalid number of inputs")

    def race(self):
        for vehicle in self.vehicles:
            vehicle.move(self.time)
        return self

    def get_winner(self):
        winner = self.vehicles[0]
        winner_dif = abs(self.path_length - winner.position % self.path_length)
        for vehicle in self.vehicles[1:]:
            dif = vehicle.position % self.path_length
            if dif == winner_dif:
                if vehicle.num < winner.num:
                    winner = vehicle
            elif dif <= winner_dif:
                winner = vehicle
                winner_dif = dif
        return winner.num


if __name__ == '__main__':
    Race().race().get_winner()














