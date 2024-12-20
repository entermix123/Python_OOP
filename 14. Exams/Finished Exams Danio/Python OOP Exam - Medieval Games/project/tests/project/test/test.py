from unittest import TestCase

from project.movie import Movie


class MovieTest(TestCase):

    def setUp(self):
        self.movie = Movie('The Dip', 1999, 9.8)

    def test_correct_init__expect_ok(self):
        self.assertEqual('The Dip', self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(9.8, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_incorrect_name__expect_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual(f"Name cannot be an empty string!", str(ve.exception))

    def test_incorrect_year__expect_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1834

        self.assertEqual(f"Year is not valid!", str(ve.exception))

    def test_add_correct_actors__expect__ok(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor('Depp')
        self.assertEqual(["Depp"], self.movie.actors)
        self.movie.add_actor('Diego')
        self.assertEqual(["Depp", "Diego"], self.movie.actors)

    def test_add_same_actors__expect__message(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor('Depp')
        result = self.movie.add_actor('Depp')
        self.assertEqual(f"Depp is already added in the list of actors!", result)

    def test_movie_rating__first_rating_greater_than_second(self):
        new_movie = Movie(f'The Brick', 2006, 8.0)

        result = self.movie > new_movie

        self.assertEqual(f'"The Dip" is better than "The Brick"', result)

    def test_movie_rating__second_rating_greater_than_first(self):
        new_movie = Movie('The Brick', 2006, 9.9)

        result = new_movie > self.movie

        self.assertEqual(f'"The Brick" is better than "The Dip"', result)

    def test__repr__(self):
        self.movie.actors = ['Depp', 'Diego']
        expected = f"Name: The Dip\n" \
                   f"Year of Release: 1999\n" \
                   f"Rating: 9.80\n" \
                   f"Cast: Depp, Diego"

        result = self.movie.__repr__()
        self.assertEqual(expected, result)
