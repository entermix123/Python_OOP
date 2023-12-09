from abc import ABC, abstractmethod     # import abstraction class and methods
from math import log2, ceil, floor      # import logarithm, ceil and floor functions


class Computer(ABC):        # create abstract class Computer

    def __init__(self, manufacturer: str, model: str):      # initialize abstract class
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None       # set processor to None
        self.ram = None             # set RAM to None
        self.price = 0              # set price to 0

    @property                       # abstract property for type of computer
    @abstractmethod
    def type(self):
        ...

    @property                       # abstract property for available processors
    @abstractmethod
    def av_processor(self):
        ...

    @property                       # abstract property for max ram
    @abstractmethod
    def max_ram(self):
        ...

    @property                       # set getter for manufacturer
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter            # set setter for manufacturer
    def manufacturer(self, value):
        if value.strip() == '':                                         # check if manufacturer name is empty
            raise ValueError("Manufacturer name cannot be empty.")      # if empty raise error

        self.__manufacturer = value                                 # if not empty assign manufacturer name

    @property                       # set getter for model
    def model(self):
        return self.__model

    @model.setter                   # set setter for model
    def model(self, value):
        if value.strip() == '':                                     # check if model name is empty
            raise ValueError("Model name cannot be empty.")         # if empty raise error

        self.__model = value                                        # if not empty assign model name

    @staticmethod                   # static method to check if RAM value is power of 2
    def power_of_two(ram: int):
        result = log2(ram)          # calculate logarithm of RAM value, but returns float always

        # check if rounded up and rounded down values are equal to find if result is valid integer number
        # see requirements
        return ceil(result) == floor(result)

    def configure_computer(self, processor: str, ram: int):     # set configure method
        if processor not in self.av_processor:                  # check if processor is in available processors

            # if processor is not in available processors raise error
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        # if ram is not power of 2 or ram is greater than max ram -> not valid parameters
        if not self.power_of_two(ram) or ram > self.max_ram:

            # raise error
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        # if ram is power of 2 and ram is not greater than max ram -> valid parameters
        self.set_parts(processor, ram)              # call set_parts method to assign parts to computer

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def set_parts(self, processor: str, ram: int):      # set set_parts method in case of valid parameters
        self.processor = processor
        self.ram = ram
        self.price += self.av_processor[processor]      # add price of processor to price of coputer
        self.price += int(log2(ram)) * 100              # add price of ram to price of computer

    def __repr__(self):                                 # return representation of computer
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
