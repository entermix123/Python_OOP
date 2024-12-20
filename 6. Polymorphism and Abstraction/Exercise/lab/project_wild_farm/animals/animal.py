from abc import ABC, abstractmethod  # import abstract method


class Animal(ABC):

    def __init__(self, name: str, weight: int):     # arguments needed fot initialization
        self.name = name
        self.weight = weight
        self.food_eaten = 0     # additional argument with default value 0

    @property                   # property that check if the food is correct for the animal
    @abstractmethod             # method must be implemented in every inherited class
    def food_that_eats(self):
        ...

    @property
    @abstractmethod             # abstract method must be implemented in every inherited class
    def gained_weight(self):    # additional function that returns gained weight after feeding
        ...

    @staticmethod           # make static method, implementation arrangement is important
    @abstractmethod         # make abstract method, implementation arrangement is important
    def make_sound():       # method must be defined in every inherited class
        ...

    def feed(self, food):                           # feed the animal with the food
        if type(food) not in self.food_that_eats:   # if food is not of the correct type
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
            # return result string

        self.weight += food.quantity * self.gained_weight       # calculate gained weight
        self.food_eaten += food.quantity                        # add food to food_eaten


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: int, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @staticmethod           # make static method, implementation arrangement is important
    @abstractmethod         # make abstract method, implementation arrangement is important
    def make_sound():       # inherited from Animal
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod           # make static method, implementation arrangement is important
    @abstractmethod         # make abstract method, implementation arrangement is important
    def make_sound():       # inherited from Animal
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
