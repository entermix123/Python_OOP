# class Shape:        # base class for polimorphic shapes
#
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):     # secondary class for rectangular shapes
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):            # secondary class for circular shapes
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#
# shapes = [Rectangle(10, 20), Circle(5)]     # list of objects
# for shape in shapes:                        # call for objects from every secondary class
#     print(shape.area())

# class MyList:
#     def __init__(self, items):
#         self.items = items
#
#     def __len__(self):
#         return len(self.items)
#
#
# my_list = MyList([1, 2, 3, 4, 5])
# print(len(my_list))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(p1)
# print(p2)
# print(p3)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# p1 = Point(5, 8)
# p2 = Point(3, 4)
# p3 = p1 - p2
# print(p1)
# print(p2)
# print(p3)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __mul__(self, other):
#         return Point(self.x * other.x, self.y * other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# p1 = Point(5, 8)
# p2 = Point(3, 4)
# p3 = p1 * p2
# print(p1)
# print(p2)
# print(p3)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __floordiv__(self, other):                          #  __floordiv__ floor division
#         return Point(self.x // other.x, self.y // other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# p1 = Point(10, 14)
# p2 = Point(3, 4)
# p3 = p1 // p2
# print(p1)
# print(p2)
# print(p3)

# def print_area(obj):            # common function
#     print(obj.get_area())       # use function form other classes


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):         # class method
#         return self.width * self.height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):             # class method
#         return 3.14 * self.radius * self.radius
#
#
# rectangle = Rectangle(10, 5)        # define class object
# circle = Circle(7)                  # define class object
#
# print(rectangle.get_area())  # use function in class to calculate area for class object
# print(circle.get_area())     # use function in class to calculate area for class object
#
# print_area(rectangle)       # use common function to calculate area for objects from different classes
# print_area(circle)          # see common function to calculate area for objects from different classes


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * 3.14 * self.radius
#
#
# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())

# my_rectangle = Rectangle(5, 3)
# circle = Circle(4)
#
# print(my_rectangle.calculate_area())
# print(circle.calculate_area())
# print(my_rectangle.calculate_perimeter())
# print(circle.calculate_perimeter())
