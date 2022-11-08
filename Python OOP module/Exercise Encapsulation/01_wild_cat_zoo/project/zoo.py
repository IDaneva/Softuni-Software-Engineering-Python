from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__animal_capacity > len(self.animals) and self.__budget - price < 0:
            return "Not enough budget"

        if self.__animal_capacity > len(self.animals) and self.__budget - price > 0:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_money = 0
        for w in self.workers:
            needed_money += w.salary

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = 0
        for a in self.animals:
            needed_money += a.money_for_care

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        animal_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        for a in self.animals:
            animal_dict[a.__class__.__name__].append(str(a))

        result.append(f"----- {len(animal_dict['Lion'])} Lions:")
        result.extend(animal_dict['Lion'])
        result.append(f"----- {len(animal_dict['Tiger'])} Tigers:")
        result.extend(animal_dict['Tiger'])
        result.append(f"----- {len(animal_dict['Cheetah'])} Cheetahs:")
        result.extend(animal_dict['Cheetah'])

        return '\n'.join(result)

    def workers_status(self):
        result =[f"You have {len(self.workers)} workers"]
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}
        for w in self.workers:
            workers_dict[w.__class__.__name__].append(str(w))

        result.append(f"----- {len(workers_dict['Keeper'])} Keepers:")
        result.extend(workers_dict['Keeper'])
        result.append(f"----- {len(workers_dict['Caretaker'])} Caretakers:")
        result.extend(workers_dict['Caretaker'])
        result.append(f"----- {len(workers_dict['Vet'])} Vets:")
        result.extend(workers_dict['Vet'])
        return '\n'.join(result)



