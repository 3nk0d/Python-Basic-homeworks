from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 60
    started: bool = False
    fuel: int = 30
    fuel_consumption: int = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not(self.started):
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        fuel_exist = self.fuel - (distance * self.fuel_consumption)
        if fuel_exist >= 0:
            self.fuel = fuel_exist
        else:
            raise NotEnoughFuel
