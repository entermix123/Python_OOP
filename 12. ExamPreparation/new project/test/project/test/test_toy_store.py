from project_pizza.project import ToyStore

import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_correct_init(self):
        for key in range(ord('A'), ord('G') + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_on_not_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('Z', "some toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_on_shelf_raises_exception(self):
        self.store.add_toy('A', "some toy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', "some toy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_on_full_shelf_raises_exception(self):
        self.store.add_toy('A', "some toy1")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', "some toy")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        result = self.store.add_toy('A', "some toy")
        self.assertEqual("Toy:some toy placed successfully!", result)
        self.assertEqual("some toy", self.store.toy_shelf['A'])

    def test_remove_toy_from_not_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('K', 'some toy')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_not_existing_name_from_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'some toy1')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.store.toy_shelf['A'] = "some toy"
        result = self.store.remove_toy('A', "some toy")
        self.assertIsNone(self.store.toy_shelf['A'])
        self.assertEqual("Remove toy:some toy successfully!", result)


if __name__ == '__main__':
    unittest.main()
