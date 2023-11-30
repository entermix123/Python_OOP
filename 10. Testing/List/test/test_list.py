import unittest

from project_python_oop_exam_christmas_pastry_shop.extended_list import IntegerList


class TestList(unittest.TestCase):

    def setUp(self):
        self.list1 = IntegerList(1, 4, 6, 7.6, 8, 9, "sdf")  # Arrange: set up list and test input condition

    def test_init(self):
        self.assertTrue(5, len(self.list1.get_data()))       # Assert: compare expected len with len of list

    def test_add_element(self):                             # test add element to list
        self.list1.add(10)                                  # Act
        self.assertEqual(6, len(self.list1.get_data()))     # Assert: compare len of list with len of result of the action
        with self.assertRaises(ValueError) as ve:           # Arrange: set ValueError
            self.list1.add('mf')                            # Act: try to add element to list that is not an integer
        self.assertEqual("Element is not Integer", str(ve.exception))   # Assert: compare expected message with actual msg

    def test_remove_element(self):                          # test remove element from list
        self.list1.remove_index(3)                          # Act: remove existing element
        self.assertEqual(4, len(self.list1.get_data()))     # Assert: compare len of list with len of result of the action
        with self.assertRaises(IndexError) as ex:           # Arrange: set IndexError
            self.list1.remove_index(10)                     # Act: try to remove element from list that is out of range
        self.assertEqual("Index is out of range", str(ex.exception))    # Assert: compare expected message with actual msg

    def test_get(self):                         # test get element from list
        result = self.list1.get(3)              # Act: execute get method Arrange: result
        self.assertEqual(8, result)             # Assert: compare expected result with actual result
        with self.assertRaises(IndexError) as ex:   # Arrange: set IndexError
            self.list1.get(10)                      # Act: try to get element from list that is out of range
        self.assertEqual("Index is out of range", str(ex.exception))    # Assert: compare expected result with actual result

    def test_insert(self):                                  # test insert element to list
        self.list1.insert(3, 10)                            # Act: execute insert method
        self.assertEqual(6, len(self.list1.get_data()))     # Assert: compare len of list with len of result of the action
        with self.assertRaises(IndexError) as ex:           # Arrange: set IndexError
            self.list1.insert(10, 3)                        # Act: try to insert element to index that is out of range
        self.assertEqual("Index is out of range", str(ex.exception))  # Assert: compare expected message with actual msg

    def test_get_biggest(self):                     # test get biggest element from list
        result = self.list1.get_biggest()           # Act: execute get_biggest method
        self.assertEqual(9, result)                 # Assert: compare expected result with actual result

    def test_get_index(self):                       # test get index element from list
        result = self.list1.get_index(4)            # Act: execute get_index method
        self.assertEqual(result, 1)                 # Assert: compare expected result with actual result


if __name__ == '__main__':
    unittest.main()
