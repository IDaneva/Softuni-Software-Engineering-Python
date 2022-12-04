
class Player:
    used_names = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.used_names:
            raise Exception(f"Name {value} is already used!")
        self.used_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > 100 or value < 0:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def needs_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.__name}, {self.__age}, {self.__stamina}, {self.needs_sustenance}"
