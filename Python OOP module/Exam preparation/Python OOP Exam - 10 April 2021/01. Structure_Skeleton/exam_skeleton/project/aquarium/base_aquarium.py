from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.__name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.__name}:",
                  f"Fish: {'none' if not self.fish else ' '.join([x.name for x in self.fish])}",
                  f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]
        return "\n".join(result)

    def calculate_value(self):
        value = 0
        for decoration in self.decorations:
            value += decoration.price

        for fish in self.fish:
            value += fish.price
        return value
        # decorations_value = [x.price for x in self.decorations]
        # fish_value = [x.price for x in self.fish]
        # return sum(decorations_value + fish_value)

    def __repr__(self):
        return f"{self.__name} fish {self.fish} cap {self.capacity} dec {self.decorations}"