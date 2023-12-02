from project_wild_farm.animals.animal import Mammal
from project_wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return f"Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 0.10             # return gained weight


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return f"Woof!"

    @property
    def food_that_eats(self):
        return [Meat]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 0.40             # return gained weight


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return f"Meow"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 0.30             # return gained weight


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return f"ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]           # for check if food in self.food_that_eats in Animals.feed()

    @property
    def gained_weight(self):
        return 1             # return gained weight

