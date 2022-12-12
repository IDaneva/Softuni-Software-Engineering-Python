from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        current_delicacy = self.delicacy_creator(type_delicacy)(name, price)
        self.delicacies.append(current_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def find_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        return False

    @staticmethod
    def delicacy_creator(type_delicacy):
        if type_delicacy == "Gingerbread":
            return Gingerbread
        if type_delicacy == "Stolen":
            return Stolen

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_booth_by_nr(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        made_booth = self.booth_creator(type_booth)(booth_number, capacity)
        self.booths.append(made_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def find_booth_by_nr(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        return False

    @staticmethod
    def booth_creator(booth_type):
        if booth_type == "Open Booth":
            return OpenBooth
        if booth_type == "Private Booth":
            return PrivateBooth

    def reserve_booth(self, number_of_people: int):
        available_booths = [x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people]
        if not available_booths:
            raise Exception(f"No available booth for {number_of_people} people!")
        found_booth = available_booths[0]
        found_booth.reserve(number_of_people)
        return f"Booth {found_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not self.find_booth_by_nr(booth_number):
            raise Exception(f"Could not find booth {booth_number}!")
        if not self.find_delicacy_by_name(delicacy_name):
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = self.find_booth_by_nr(booth_number)
        delicacy = self.find_delicacy_by_name(delicacy_name)
        booth.make_an_order(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_nr(booth_number)
        bill = booth.price_for_reservation + sum([x.price for x in booth.delicacy_orders])
        self.income += bill
        booth.clear_booth()
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

