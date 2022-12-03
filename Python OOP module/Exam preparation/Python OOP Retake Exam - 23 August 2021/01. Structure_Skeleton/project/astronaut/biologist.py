from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5
