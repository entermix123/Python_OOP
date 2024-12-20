#
# def number_increment(numbers):
#     def increase():
#         # TODO: Implement
#         return [x + 1 for x in numbers]
#     return increase()
#
#
# print(number_increment([1, 2, 3]))
from Tools.scripts.texi2html import increment


def increment_decorator(func):              # function as argument
    def wrapper(numbers):                   # inner function (wrapper) of the decorator
        numbers = [n + 1 for n in numbers]  # action of the inner function
        return func(numbers)                # return the number like result of the received function
    return wrapper                          # return the result of the inner (wrapper) function


@increment_decorator            # create outside function increment decorator that uses function number_increment as argument
def number_increment(numbers):
    return numbers


print(number_increment([1, 2, 3]))
