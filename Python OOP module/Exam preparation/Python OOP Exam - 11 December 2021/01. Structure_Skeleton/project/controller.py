from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [x.model for x in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type in ["MuscleCar", "SportsCar"]:
            car = Controller.car_creator(car_type)(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    @staticmethod
    def car_creator(car_type):
        if car_type == "MuscleCar":
            return MuscleCar
        if car_type == "SportsCar":
            return SportsCar

    def found_driver(self, driver_name: str):
        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            return False
        return driver

    def found_race(self, race_name):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            return False
        return race

    def create_driver(self, driver_name: str):
        if self.found_driver(driver_name):
            raise Exception(f"Drive {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    # тук може да има грешка за първия х
    def create_race(self, race_name: str):
        if self.found_race(race_name):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.found_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = self.found_driver(driver_name)
        cars = [x for x in self.cars if x.__class__.__name__ in ["MuscleCar", "SportsCar"] and not x.is_taken]
        if not cars:
            raise Exception(f"Car {car_type} could not be found!")
        new_car = cars[-1]
        if driver.car is not None:
            previous_car = driver.car
            driver.car = new_car
            new_car.is_taken = True
            previous_car.is_taken = False
            return f"Driver {driver_name} changed his car from {previous_car.model} to {driver.car.model}."

        if driver.car is None:
            driver.car = new_car
            new_car.is_taken = True
            return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.found_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = self.found_race(race_name)

        if not self.found_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = self.found_driver(driver_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.found_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = self.found_race(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        race_drivers = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        first_three = race_drivers[:3]

        result = []
        for driver in first_three:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
        return "\n".join(result)
