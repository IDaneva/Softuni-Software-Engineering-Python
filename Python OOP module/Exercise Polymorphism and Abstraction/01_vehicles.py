from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self.ac_on):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.ac_on)

    @abstractmethod
    def refuel(self, fuel):
        pass

    @property
    @abstractmethod
    def ac_on(self):
        pass


class Car(Vehicle):
    @property
    def ac_on(self):
        return 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    @property
    def ac_on(self):
        return 1.6

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


car = Car(20, 5)

car.drive(3)

print(car.fuel_quantity)

car.refuel(10)

print(car.fuel_quantity)

truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)