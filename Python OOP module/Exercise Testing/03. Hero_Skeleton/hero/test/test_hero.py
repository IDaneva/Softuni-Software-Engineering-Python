import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Perry the Platypus", 75, 100, 1)
        self.enemy = Hero("dr. Doofenschmirtz", 70, 50, 1)

    def test_initialization(self):
        self.assertEqual("Perry the Platypus", self.hero.username)
        self.assertEqual(75, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(1, self.hero.damage)

    def test_battle_method_when_fighting_with_ourselves_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_when_hero_health_is_low_expect_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_when_enemy_health_is_low_expect_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight dr. Doofenschmirtz. He needs to rest", str(ve.exception))

    def test_battle_method_with_proper_stats_and_draw_result(self):
        self.hero.health = 5
        self.enemy.health = 5
        result = self.hero.battle(self.enemy)
        self.assertEqual(-65, self.hero.health)
        self.assertEqual(-70, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_method_when_enemy_health_becomes_zero_or_negative(self):
        self.enemy.health = 5
        result = self.hero.battle(self.enemy)
        self.assertEqual(76, self.hero.level)
        self.assertEqual(35, self.hero.health)
        self.assertEqual(6, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_when_hero_health_becomes_zero_or_negative(self):
        self.hero.health = 25
        self.enemy.health = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual(71, self.enemy.level)
        self.assertEqual(30, self.enemy.health)
        self.assertEqual(6, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_string_representation_of_hero(self):
        self.assertEqual("Hero Perry the Platypus: 75 lvl\n"
                         "Health: 100\n"
                         "Damage: 1\n", str(self.hero))


if __name__ == "__main__":
    unittest.main()
