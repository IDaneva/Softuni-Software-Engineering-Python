from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATH = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15
