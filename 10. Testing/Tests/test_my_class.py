import unittest

from project_python_oop_exam_christmas_pastry_shop.my_class import MyClass


class TestMyClass(unittest.TestCase):
    def setUp(self) -> None:            # set up method for testing
        self.my_object = MyClass()      # create instance of MyClass for testing

    def test_method1(self):
        result = self.my_object.method1()   # testing method1 with self.my_object
        self.assertEqual(result, "Hello")   # compare result with expected result

    def test_method2(self):
        result = self.my_object.method2()   # testing method2 with self.my_object
        self.assertEqual(result, 56)        # compare result with expected result


if __name__ == '__main__':
    unittest.main()
