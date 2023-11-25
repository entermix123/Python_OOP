# class Person:
#     kind = 'mammal'
#
#     def __init__(self, age: int):
#         self.age = age
#
#     def increase_age(self, age: int):   # this method is class method, because has self argument
#         self.age += age
#
#     @staticmethod                       # static method, because has no self input
#     def is_adult(age):
#         return age >= 18
#
# person = Person(18)
# print(person.is_adult(16))

# from typing import List
#
#
# class Pizza:
#
#     def __init__(self, ingredients: List[str]):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#
#     @classmethod
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
#
#
# first_pizza = Pizza.pepperoni()
# second_pizza = Pizza.quattro_formaggi()
# third_pizza = Pizza(["tomato sauce", "parmesan", "pepperoni"])


# # remind all important cations with class and static methods
#
# import math
#
#
# class Number:
#
#     def __init__(self, number: int):
#         self.number = number
#
#     def increase_with_root(self):
#         self.number += self.get_root(self.number)
#
#     @staticmethod               # does not have self input, can't modify class instances and objects
#     def get_root(number: int):  # do not have self argument, cannot call class methods
#         return math.sqrt(number)
#
#     @classmethod                # have cls input, universal for classes,
#     def from_float(cls, float_number: float):   # can call static methods and other class methods, can start recursion!
#         return cls(int(float_number))           # returns a class instance
#
#     def __repr__(self):
#         return str(self.number)
#
#
# print(Number.get_root(49))
# a = Number.from_float(121.5)
# print(a)
#
# print(a.get_root(49))
# a.increase_with_root()
# print(a)
#
# type prop for start getter methods
# type props for start getter and setter methods
# type propsd for start getter, setter adn delete methods
#

# # CUSTOM REDUCE FUNCTION
# from collections import deque
#
#
# def custom_reduce(func, elements):  # in this case func is lambda x, y: x + y
#     elements = deque(elements)    # using deque because can take args and put args in left side of the collection
#     arguments_count = func.__code__.co_argcount  # take count of elements in collection
#
#     while len(elements) > 1:
#         arguments = [elements.popleft() for _ in range(arguments_count)]
#         elements.appendleft(func(*arguments))
#         # popped first 2 arguments, because func using only 2 --> lambda x, y: x + y
#         # sum them and add the result to the left side of the deque --> [3, 3]
#         # next cycle sum last two elements and add result to the right side of the deque --> [6]
#         # in deque is only one element, cycle end and return it --> [6]
#
#     return elements[0]  # return the only element in the deque
#
#
# print(custom_reduce(lambda x, y: x + y, [1, 2, 3]))  # using lambda
