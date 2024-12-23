from typing import List

from project.jockey import Jockey


class HorseRace:
    VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: List[Jockey] = []

    def __str__(self):
        return self.race_type

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):

        if value not in self.VALID_RACE_TYPES:
            raise ValueError("Race type does not exist!")

        self.__race_type = value
