class Zoo:
    __animals = 0

    def __init__(self, name_of_animals):
        self.name = name_of_animals
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)} \n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)} \n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)} \n"

        result += f"Total animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for current_info in range(number_of_lines):
    info = input().split()
    species = info[0]
    name = info[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info())