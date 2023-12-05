from abc import ABC, abstractmethod


class Shape(ABC):       # made abstract class

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod             # create abstract method for area calculation
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def calculate_area(self):
        return self.width * self.height / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(shapes, list):    # check if shapes is list
            raise ValueError("`shapes` should be of type `list`")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:            # iterate through shapes list
            total += shape.calculate_area()  # calculate area

        return total    # return total area


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
