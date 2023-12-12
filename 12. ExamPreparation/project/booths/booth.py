from abc import ABC, abstractmethod
from typing import List

from project_python_oop_exam_christmas_pastry_shop.delicacies.delicacy import Delicacy


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        else:
            self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int) -> None:
        pass

