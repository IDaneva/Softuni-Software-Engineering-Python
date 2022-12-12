from abc import ABC, abstractmethod

from project.delicacies.delicacy import Delicacy


class Booth(ABC):

    @abstractmethod
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0.0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    def make_an_order(self, delicacy: Delicacy):
        self.delicacy_orders.append(delicacy)

    def clear_booth(self):
        self.delicacy_orders = []
        self.price_for_reservation = 0.0
        self.is_reserved = False
