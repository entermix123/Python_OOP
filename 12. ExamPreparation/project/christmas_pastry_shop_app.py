from typing import List

from project_python_oop_exam_christmas_pastry_shop.booths.booth import Booth
from project_python_oop_exam_christmas_pastry_shop.booths.open_booth import OpenBooth
from project_python_oop_exam_christmas_pastry_shop.booths.private_booth import PrivateBooth
from project_python_oop_exam_christmas_pastry_shop.delicacies.delicacy import Delicacy
from project_python_oop_exam_christmas_pastry_shop.delicacies.gingerbread import Gingerbread
from project_python_oop_exam_christmas_pastry_shop.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}           # define valid delicacies
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}     # define valid booths

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        delicacy = [x for x in self.delicacies if x.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = [x for x in self.booths if x.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        try:
            booth = next(filter(lambda x: x.capacity >= number_of_people and not x.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")
        try:
            delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        # booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        price_food = sum(x.price for x in booth.delicacy_orders)
        price_total = booth.price_for_reservation + price_food
        self.income += price_total
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\n" \
               f"Bill: {price_total:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
