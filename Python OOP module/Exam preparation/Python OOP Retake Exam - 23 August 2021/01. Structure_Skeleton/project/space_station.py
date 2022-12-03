from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        astronaut = SpaceStation.astronaut_creator(astronaut_type)(name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    @staticmethod
    def astronaut_creator(astronaut_type):
        if astronaut_type == "Biologist":
            return Biologist

        if astronaut_type == "Geodesist":
            return Geodesist

        if astronaut_type == "Meteorologist":
            return Meteorologist

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        items_list = items.split(", ")
        planet = Planet(name)
        planet.items.extend(items_list)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")
        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astr in self.astronaut_repository.astronauts:
            astr.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")
        planet = self.planet_repository.find_by_name(planet_name)
        suitable_astronauts = list(filter(lambda a: a.oxygen >= 30, self.astronaut_repository.astronauts))
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        sorted_astr = sorted(suitable_astronauts, key=lambda x: -x.oxygen)
        if len(sorted_astr) > 5:
            sorted_astr = sorted_astr[:5]

        participated = []
        completed = False
        for astronaut in sorted_astr:
            if not planet.items:
                self.completed_missions += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{len(participated)} astronauts participated in collecting items."
            participated.append(astronaut)
            while True:
                if not planet.items:
                    self.completed_missions += 1
                    return f"Planet: {planet_name} was explored. " \
                           f"{len(participated)} astronauts participated in collecting items."
                if astronaut.oxygen - astronaut.BREATH < 0:
                    break
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        self.not_completed_missions += 1
        return f"Mission is not completed."

    def report(self):
        result = [f"{self.completed_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  f"Astronauts' info:"]
        result.extend([str(x) for x in self.astronaut_repository.astronauts])
        return "\n".join(result)

