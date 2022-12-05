from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if self.found_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in ["Bread", "Cake"]:
            made_food = self.food_creator(food_type)(name, price)
            self.food_menu.append(made_food)
            return f"Added {name} ({food_type}) to the food menu"

    def found_food_by_name(self, food_name):
        try:
            food = next(filter(lambda f: f.name == food_name, self.food_menu))
        except StopIteration:
            return False
        return food

    @staticmethod
    def food_creator(food_type):
        if food_type == "Bread":
            return Bread
        if food_type == "Cake":
            return Cake

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.found_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in ["Water", "Tea"]:
            made_drink = self.drink_creator(drink_type)(name, portion, brand)
            self.drinks_menu.append(made_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def found_drink_by_name(self, drink_name):
        try:
            drink = next(filter(lambda d: d.name == drink_name, self.drinks_menu))
        except StopIteration:
            return False
        return drink

    @staticmethod
    def drink_creator(drink_type):
        if drink_type == "Tea":
            return Tea
        if drink_type == "Water":
            return Water

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.found_table_by_nr(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type in ["InsideTable", "OutsideTable"]:
            table = self.table_creator(table_type)(table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def found_table_by_nr(self, number):
        try:
            table = next(filter(lambda t: t.table_number == number, self.tables_repository))
        except StopIteration:
            return False
        return table

    @staticmethod
    def table_creator(table_type):
        if table_type == "InsideTable":
            return InsideTable
        if table_type == "OutsideTable":
            return OutsideTable

    def reserve_table(self, number_of_people: int):
        available_tables = [x for x in self.tables_repository
                            if x.capacity >= number_of_people
                            and not x.is_reserved
                            and x.number_of_people == 0]
        if not available_tables:
            return f"No available table for {number_of_people} people"
        first_found = available_tables[0]
        first_found.reserve(number_of_people)
        return f"Table {first_found.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        if not self.found_table_by_nr(table_number):
            return f"Could not find table {table_number}"
        table = self.found_table_by_nr(table_number)

        ordered = []
        missing = []

        for food_name in food_names:
            if not self.found_food_by_name(food_name):
                missing.append(food_name)
                continue

            found_food = self.found_food_by_name(food_name)
            ordered.append(found_food)
            table.order_food(found_food)

        result = [f"Table {table_number} ordered:"]
        result.extend([x.__repr__() for x in ordered])
        result.append(f"{self.name} does not have in the menu:")
        result.extend([x for x in missing])
        return "\n".join(result)

    def order_drink(self, table_number: int, *drink_names):
        if not self.found_table_by_nr(table_number):
            return f"Could not find table {table_number}"
        table = self.found_table_by_nr(table_number)

        ordered = []
        missing = []

        for drink_name in drink_names:
            if not self.found_drink_by_name(drink_name):
                missing.append(drink_name)
                continue

            found_drink = self.found_drink_by_name(drink_name)
            ordered.append(found_drink)
            table.order_drink(found_drink)
        result = [f"Table {table_number} ordered:"]
        result.extend([x.__repr__() for x in ordered])
        result.append(f"{self.name} does not have in the menu:")
        result.extend([x for x in missing])
        return "\n".join(result)

    def leave_table(self, table_number: int):
        if not self.found_table_by_nr(table_number):
            return
        table = self.found_table_by_nr(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        result = [f"Table: {table.table_number}", f"Bill: {bill:.2f}"]
        return "\n".join(result)

    def get_free_tables_info(self):
        tables = [x.free_table_info() for x in self.tables_repository if not x.is_reserved and x.number_of_people == 0]
        return "\n".join(tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
