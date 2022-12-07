from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return f"Invalid aquarium type."

        aquarium = self.aquarium_creator(aquarium_type)(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    @staticmethod
    def aquarium_creator(aquarium_type):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium
        if aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium

    @staticmethod
    def decorations_creator(decoration_type):
        if decoration_type == "Ornament":
            return Ornament
        if decoration_type == "Plant":
            return Plant

    @staticmethod
    def fish_creator(fish_type):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish
        if fish_type == "SaltwaterFish":
            return SaltwaterFish

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return f"Invalid decoration type."

        made_decoration = self.decorations_creator(decoration_type)()
        self.decorations_repository.add(made_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decorations = [x for x in self.decorations_repository.decorations if x.__class__.__name__ == decoration_type]

        if not decorations:
            return f"There isn't a decoration of type {decoration_type}."

        try:
            aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums))
        except StopIteration:
            return

        aquarium.add_decoration(decorations[0])
        self.decorations_repository.remove(decorations[0])
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        fish = self.fish_creator(fish_type)(fish_name, fish_species, price)
        try:
            aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums))
        except StopIteration:
            return

        if aquarium.suitable_for_fish != fish_type:
            return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        try:
            aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums))
        except StopIteration:
            return
        aquarium.feed()
        return f"Fish fed: {len([x for x in aquarium.fish])}"

    def calculate_value(self, aquarium_name):
        try:
            aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums))
        except StopIteration:
            return

        result = aquarium.calculate_value()
        return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        aqua_info = [str(x) for x in self.aquariums]
        return "\n".join(aqua_info)
