from unittest import TestCase

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer('lildanio', 25, 15.0)

    def test__init__(self):
        self.assertEqual('lildanio', self.player.name)
        self.assertEqual(25, self.player.age)
        self.assertEqual(15.0, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_wrong_name__expect_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'k'

        expected_msg = "Name should be more than 2 symbols!"
        self.assertEqual(expected_msg, str(ve.exception))

    def test_wrong_age__expect_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15

        expected_msg = "Players must be at least 18 years of age!"
        self.assertEqual(expected_msg, str(ve.exception))

    def test_add_new_win__expect_ok(self):
        tournament_name = 'mahlata'
        self.player.add_new_win(tournament_name)
        tournament_name2 = 'selskee'
        self.player.add_new_win(tournament_name2)
        self.assertEqual(['mahlata', 'selskee'], self.player.wins)

    def test_add_new_win_with_existing_win__expect_mas(self):
        self.player.wins = ['mahlata']
        tournament_name = 'mahlata'
        result = self.player.add_new_win(tournament_name)
        expected_msg = f"mahlata has been already added to the list of wins!"
        self.assertEqual(expected_msg, result)
        self.assertEqual(['mahlata'], self.player.wins)

    def test_lt_self_lower_than_other(self):
        self.player2 = TennisPlayer('lilshet', 23, 16)

        result = self.player < self.player2
        expected_msg = f'lilshet is a top seeded player and he/she is better than lildanio'
        self.assertEqual(expected_msg, result)

    def test_lt_other_lower_than_self(self):
        self.player2 = TennisPlayer('lilshet', 23, 13)

        result = self.player < self.player2
        expected_msg = f'lildanio is a better player than lilshet'
        self.assertEqual(expected_msg, result)

    def test_str__expect_msg(self):
        self.player.wins = ['mahlata', 'naselo']
        expected_msg = f"Tennis Player: lildanio\n" \
               f"Age: 25\n" \
               f"Points: 15.0\n" \
               f"Tournaments won: mahlata, naselo"

        self.assertEqual(expected_msg, str(self.player))
