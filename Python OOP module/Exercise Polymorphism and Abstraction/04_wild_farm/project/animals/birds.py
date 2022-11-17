from project.animals.animal import Bird
from project.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def eaten_food(self):
        return [Meat]

    def weight_increase(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def eaten_food(self):
        return [Meat, Seed, Fruit, Vegetable]

    def weight_increase(self):
        return 0.35
