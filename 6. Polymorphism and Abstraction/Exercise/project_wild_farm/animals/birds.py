from project_wild_farm.animals.animal import Bird
from project_wild_farm.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return f"Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 0.25             # return gained weight


class Hen(Bird):

    @staticmethod
    def make_sound():
        return f"Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 0.35             # return gained weight
