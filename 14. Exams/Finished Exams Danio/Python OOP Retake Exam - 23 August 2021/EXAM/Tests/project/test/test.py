from unittest import TestCase

from project.library import Library


class TestLibrary(TestCase):

    def setUp(self):
        self.lib = Library('name1')
        # self.books_by_authors = {'Elvis': 'the thing'}
        # self.readers = {'lilreader': 'read'}

    def test_init(self):
        self.assertEqual('name1', self.lib.name)
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_empty_name__expect_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.lib.name = ''
        expected_msg = "Name cannot be empty string!"

        self.assertEqual(expected_msg, str(ve.exception))

    def test_add_book__expect_ok(self):
        self.lib.add_book('Elvis', 'the thing')
        self.assertEqual({'Elvis': ['the thing']}, self.lib.books_by_authors)

    def test_add_reader_expect_msg(self):
        self.lib.add_reader('lilreader')
        self.assertEqual({'lilreader': []}, self.lib.readers)

        result = self.lib.add_reader('lilreader')
        expected_msg = f"lilreader is already registered in the name1 library."
        self.assertEqual(expected_msg, result)

    def test_rent_book_not_in_lib__expect_msg(self):
        self.lib.add_book('Elvis', 'the thing')
        reader_name = 'lilreader'
        expected_msg = f"lilreader is not registered in the name1 Library."
        self.assertEqual(expected_msg, self.lib.rent_book('lilreader', 'Elvis', 'the thong'))

    def test_rent_book__with_book_not_in_lib__expect_msg(self):
        self.lib.add_book('Elvis', 'the thing')
        self.lib.readers = {'lilreader': []}
        book_name = 'the shet'
        book_author = 'Karavelov'
        expected_msg = f"name1 Library does not have any Karavelov's books."
        self.assertEqual(expected_msg, self.lib.rent_book('lilreader', 'Karavelov', 'the shet'))

    def test_rent_book__with_book_title_not_in_lib__expect_msg(self):
        self.lib.add_book('Elvis', 'the thing')
        self.lib.readers = {'lilreader': []}
        # self.assertEqual({'the thing': ['Elvis']}, self.lib.books_by_authors)
        book_name = 'the shet'
        expected_msg = f"""name1 Library does not have Elvis's "the shet"."""
        self.assertEqual(expected_msg, self.lib.rent_book('lilreader', 'Elvis', 'the shet'))

    def test_rent_book_successfully__expect_ok_reader_list(self):
        self.lib.readers = {'lilreader': []}
        self.lib.add_book('Elvis', 'the thing')
        self.lib.rent_book('lilreader', 'Elvis', 'the thing')
        self.assertEqual([{'Elvis': 'the thing'}], self.lib.readers['lilreader'])