import unittest

from project_python_oop_exam_christmas_pastry_shop.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('Kaloqn', 1, 100, 100)     # Arrange
        self.enemy = Hero('Enemy', 1, 50, 50)       # Arrange

    def test_init(self):
        self.assertEqual('Kaloqn', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_with_yourself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_self_low_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_with_low_health_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_heroes_calculating_damage(self):
        self.assertEqual(100, self.hero.damage * self.hero.level)
        self.assertEqual(50, self.enemy.damage * self.enemy.level)

    def test_battle_heroes_calculating_health(self):
        self.assertEqual(50, self.hero.health - self.enemy.damage)
        self.assertEqual(-50, self.enemy.health - self.hero.damage)

    def test_battle_draw(self):
        self.hero.health = 50       # Arrange
        self.enemy.health = 100     # Arrange
        self.assertEqual("Draw", self.hero.battle(self.enemy))  # Act and Assert

    def test_battle_my_hero_level_up_health_up_and_damage_up_after_battle(self):
        self.hero.battle(self.enemy)                # Act
        self.assertEqual(2, self.hero.level)        # Assert
        self.assertEqual(105, self.hero.damage)     # Assert
        self.assertEqual(55, self.hero.health)      # Assert

    def test_battle_result_when_my_hero_win(self):
        self.assertEqual("You win", self.hero.battle(self.enemy))  # Assert

    def test_battle_enemy_hero_level_up_health_up_and_damage_up_after_battle(self):
        self.hero.health = 50
        self.enemy.health = 110
        self.hero.battle(self.enemy)                # Act
        self.assertEqual(2, self.enemy.level)       # Assert
        self.assertEqual(55, self.enemy.damage)     # Assert
        self.assertEqual(15, self.enemy.health)     # Assert

    def test_battle_result_when_enemy_hero_win(self):
        self.hero.health = 50
        self.enemy.health = 110
        self.assertEqual("You lose", self.hero.battle(self.enemy))  # Assert

    def test_str(self):
        self.assertEqual("Hero Kaloqn: 1 lvl\n" + "Health: 100\n" + "Damage: 100\n", str(self.hero))


if __name__ == '__main__':
    unittest.main()
