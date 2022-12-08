from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = [*children]
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        for _ in range(len(children)):
            self.appliances.append(Laptop())
            self.appliances.append(TV())
            self.appliances.append(Fridge())
        self.calculate_expenses(self.children)
        self.calculate_expenses(self.appliances)
