#
# def multiply(a, b):     # function to multiply two numbers
#     return a * b
#
#
# def add(a, b):     # function to add two numbers
#     return a + b
#
#
# def subtract(a, b):     # function to subtract two numbers
#     return a - b
#
#
# def divide(a, b):     # function to divide two numbers
#     if b == 0 or a == 0:
#         raise ValueError('Cannot divide by zero')
#     return a / b

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


import unittest


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person("Luc", "Peterson", 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
