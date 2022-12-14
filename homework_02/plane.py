"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo = 50):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        weight = cargo + self.cargo
        if weight <= self.max_cargo:
            self.cargo = weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

