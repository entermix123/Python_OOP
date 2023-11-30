# impoself=Nonest     # import testing
#
#
# def multiply(a, b):     # function to multiply two numbers
#     return a * b
#
#
# class TestMultiply(unittest.TestCase):          # create class for testing
#     def test_multiply(self):                    # create function for testing
#         self.assertEqual(multiply(2, 3), 5)     # test if function works properly
#         self.assertEqual(multiply(3, 3), 9)     # test if function works properly
#
#
# if __name__ == '__main__':      # execute module test
#     unittest.main()


# import unittest     # import testing
#
# from example2 import add, subtract, multiply, divide        # import functions that should be tested
#
#
# class TestMyMath(unittest.TestCase):          # create class for testing
#     def test_add(self):                    # create function for testing
#         self.assertEqual(add(2, 3), 5)     # test if function works properly
#         self.assertEqual(add(-2, 3), 1)     # test if function works properly
#
#     def test_subtract(self):                    # create function for testing
#         self.assertEqual(subtract(2, 3), -1)     # test if function works properly
#         self.assertEqual(subtract(10, 5), 5)     # test if function works properly
#
#     def test_multiply(self):                    # create function for testing
#         self.assertEqual(multiply(2, 3), 6)     # test if function works properly
#         self.assertEqual(multiply(3, 3), 9)     # test if function works properly
#
#     def test_divide(self):                    # create function for testing
#         self.assertEqual(divide(6, 3), 2)     # test if function works properly
#         self.assertEqual(divide(3, 3), 1)     # test if function works properly
#
#
# if __name__ == '__main__':      # execute module test
#     unittest.main()

# import unittest     # import testing
#
#
# class MyTest(unittest.TestCase):        # test class inherit unittest.TestCase
#
#     def test_addition(self):
#         result = 2 + 2
#         self.assertEqual(result, 4)
#
#     def test_subtraction(self):
#         result = 5 - 3
#         self.assertEqual(result, 2)
#
#     def test_multiplication(self):
#         result = 2 * 3
#         self.assertEqual(result, 6)
#
#     def test_division(self):
#         result = 6 / 3
#         self.assertEqual(result, 2)
#
#
# if __name__ == '__main__':      # called to run all tests in the class
#     unittest.main()

# import unittest
# import time
#
#
# class MyTest(unittest.TestCase):
#
#     def test_something(self):
#         start_time = time.time()
#         time.sleep(1)                   # tested function
#         end_time = time.time()
#         diff = end_time - start_time
#         print(f"Test took time {diff} seconds to complete")
#         self.assertTrue(True)
#
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
#
#
# def add_numbers(a, b):                  # function add to test
#     return a + b
#
#
# def is_even(num):
#     return num % 2 == 0
#
#
# class MyTest(unittest.TestCase):        # test class inherit unittest.TestCase
#
#     def test_add_positive(self):        # create test function with positive parameters (custom conditions)
#         result = add_numbers(2, 3)      # generate result with original function
#         self.assertEqual(result, 5)     # compare result with expected result
#
#     def test_add_negative(self):
#         result = add_numbers(-2, -3)
#         self.assertNotEqual(result, -7)  # compare result with expected result but with NOT -> 'assertNotEqual'
#
#     def test_add_positive_true(self):
#         result = add_numbers(-2, -3)
#         self.assertTrue(result, -5)      # compare result with expected result and return True or False
#
#     def test_is_even(self):
#         self.assertTrue(is_even(2))      # execute the function with custom parameter and return True or False
#         self.assertTrue(is_even(4))      # execute the function with custom parameter and return True or False
#         self.assertTrue(is_even(22))     # execute the function with custom parameter and return True or False
#
#     def test_is_odd(self):
#         self.assertFalse(is_even(1))      # execute the function with custom parameter and return False if not even
#         self.assertFalse(is_even(5))      # execute the function with custom parameter and return False if not even
#         self.assertFalse(is_even(77))     # execute the function with custom parameter and return False if not even
#
#
# if __name__ == '__main__':
#     unittest.main()         # main test class
#

# import unittest
#
#
# def get_common_elemnts(list1, list2):
#     return set(list1).intersection(list2)
#
#
# class MyTest(unittest.TestCase):
#     def test_common_elements_in(self):
#         list1 = [1, 2, 3, 4, 5]
#         list2 = [4, 5, 6, 7, 8]
#         result = get_common_elemnts(list1, list2)
#         self.assertEqual(4, result)
#         self.assertIn(5, result)
#
#     def test_common_elements_not_in(self):
#         list1 = [1, 2, 3]
#         list2 = [4, 5, 6]
#         result = get_common_elemnts(list1, list2)
#         self.assertNotEqual(4, result)
#         self.assertNotIn(5, result)
#
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
#
#
# def divide_numbers(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Cannot divide by zero')
#     return a / b
#
#
# class MyTest(unittest.TestCase):
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide_numbers(2, 0)        # OK
#             # divide_numbers(4, 1)        # NOT OK
#
#     def test_divide_positive(self):
#         self.assertEqual(divide_numbers(10, 5), 2.0)  # OK
#
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
#
#
# class MyClass:
#
#     def method1(self):
#         return "Hello"
#
#     def method2(self):
#         return 56
#
#
# class TestMyClass(unittest.TestCase):
#     def setUp(self) -> None:            # set up method for testing
#         self.my_object = MyClass()      # create instance of MyClass for testing
#
#     def test_method1(self):
#         result = self.my_object.method1()   # testing method1 with self.my_object
#         self.assertEqual(result, "Hello")   # compare result with expected result
#
#     def test_method2(self):
#         result = self.my_object.method2()   # testing method2 with self.my_object
#         self.assertEqual(result, 56)        # compare result with expected result
#
#
# if __name__ == '__main__':
#     unittest.main()

