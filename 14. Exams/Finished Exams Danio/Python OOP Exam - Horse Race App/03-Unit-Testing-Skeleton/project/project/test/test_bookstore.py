from unittest import TestCase, main

from project.bookstore import Bookstore


class Test(TestCase):
    # Act
    def test_init__expect_ok(self):
        store = Bookstore(5)

        # assert
        self.assertEqual(5, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store._Bookstore__total_sold_books)

    def test_correct_limit__expect_ok(self):
        store = Bookstore(5)
        store.books_limit = 3
        self.assertEqual(3, store.books_limit)

    def test_negative_and_0__limit__expect_raise_exception(self):
        store = Bookstore(5)
        with self.assertRaises(ValueError) as ex:
            store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            store.books_limit = -3
        self.assertEqual("Books limit of -3 is not valid", str(ex.exception))

    def test_class_len__expect_ok(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            'book1': 4,
            'book2': 3,
            'book3': 2,
        }
        self.assertEqual(9, len(store))

    def test_receive_book_over__expect_raise_exception(self):
        store = Bookstore(10)
        with self.assertRaises(Exception) as ex:
            store.receive_book("The Hobbit", 13)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book__expect_correct_message(self):
        store = Bookstore(10)
        result = store.receive_book('The Drop', 3)
        expected_message = "3 copies of The Drop are available in the bookstore."
        self.assertEqual(expected_message, result)

    def test_receive_book__expect_correct_dict_from_availability(self):
        store = Bookstore(10)
        store.receive_book('The Drop', 3)
        message = {'The Drop': 3}
        self.assertEqual(message, store.availability_in_store_by_book_titles)

        store.receive_book('The Pinch', 3)
        message2 = {'The Drop': 3, 'The Pinch': 3}
        self.assertEqual(message2, store.availability_in_store_by_book_titles)

    def test_sell_book_successful__expect_updated_dict(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {'The Drop': 3}
        result = store.sell_book('The Drop', 1)
        message = "Sold 1 copies of The Drop"
        self.assertEqual(message, result)

    def test_sell_book_not_successful__expect_raise_exception(self):
        store = Bookstore(10)
        store.receive_book('The Drop', 3)

        with self.assertRaises(Exception) as ex:
            store.sell_book('The Drop', 4)

        self.assertEqual("The Drop has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_not_successful__except_raise_exception(self):
        store = Bookstore(10)
        store.receive_book('The Drop', 3)

        with self.assertRaises(Exception) as ex:
            store.sell_book('some book', 2)

        self.assertEqual(f"Book some book doesn't exist!", str(ex.exception))

    def test_class_str__except_ok(self):
        store = Bookstore(10)
        store.receive_book('The Drop', 3)
        expected_result = (f'Total sold books: 0\n'
                           'Current availability: 3\n'
                           ' - The Drop: 3 copies')

        self.assertEqual(expected_result, str(store))

    if __name__ == "__main__":
        main()
