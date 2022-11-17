from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def eaten_food(self):
        return [Vegetable, Fruit]

    def weight_increase(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def eaten_food(self):
        return [Meat]

    def weight_increase(self):
        return 0.40


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def eaten_food(self):
        return [Meat, Vegetable]

    def weight_increase(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def eaten_food(self):
        return [Meat]

    def weight_increase(self):
        return 1.00

