from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 60
    started: bool = False
    fuel: int = 30
    fuel_consumtion: int = 1

    def __init__(self, weight, started , fuel, fuel_consumtion):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumtion = fuel_consumtion

    def start(self):
        if not(self.started):
            if self.fuel > 0:
                self.started = True
            raise LowFuelError

    def move(self, distance):
        fuel_exist = self.fuel - (distance * self.fuel_consumtion)
        if fuel_exist >= 0:
            self.fuel = fuel_exist
        raise NotEnoughFuel
