from project.animal import Animal


class Cat(Animal):

    def __init__(self, name: str, age: int, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"
