from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*args: List[int or float]):
        return reduce(lambda x, y: x * y, args)     # reduce is continuous function.

    @staticmethod
    def divide(*args: List[int or float]):
        return reduce(lambda x, y: x + y if x == 0 and y == 0 else x / y, args)     # escape divide by zero error

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y , args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
