from abc import ABC, abstractmethod
from typing import List


class Musician(ABC):

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills: List = []
        self.available_skills_to_learn: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Musician name cannot be empty!")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        else:
            self.__age = value

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.available_skills_to_learn:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        if new_skill not in self.skills:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."


