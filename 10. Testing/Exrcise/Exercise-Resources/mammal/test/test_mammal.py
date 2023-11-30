import unittest
from project_python_oop_exam_christmas_pastry_shop.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self):
        self.animal1 = Mammal('patladqk', 'alien', 'cluck, cluck')      # executes for every test
        # Arrange - create instance of the tested class

    def test_correct_initializing(self):
        self.assertEqual('patladqk', self.animal1.name)
        self.assertEqual('alien', self.animal1.type)
        self.assertEqual('cluck, cluck', self.animal1.sound)

    def test_make_sound_returns_correct_message(self):
        self.assertEqual('patladqk makes cluck, cluck', self.animal1.make_sound())

    def test_if_get_kingdom_returns_kingdom(self):
        self.assertEqual('animals', self.animal1.get_kingdom())

    def test_if_info_returns_correct_info(self):
        self.assertEqual("patladqk is of type alien", self.animal1.info())


if __name__ == '__main__':
    unittest.main()
