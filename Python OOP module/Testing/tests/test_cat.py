import unittest

from Testing.codes.cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self):
        self.kitty = Cat("Pisko")

    def test_proper_initialization(self):
        self.assertEqual("Pisko", self.kitty.name)
        self.assertFalse(self.kitty.fed)
        self.assertFalse(self.kitty.sleepy)
        self.assertEqual(0, self.kitty.size)

    def test_eating_method_when_kitty_is_fed(self):
        self.kitty.fed = True
        with self.assertRaises(Exception) as ex:
            self.kitty.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eating_method_when_kitty_is_hungry(self):
        self.kitty.eat()

        self.assertTrue(self.kitty.fed)
        self.assertTrue(self.kitty.sleepy)
        self.assertEqual(1, self.kitty.size)

    def test_sleep_method_when_kitty_is_hungry(self):
        with self.assertRaises(Exception) as ex:
            self.kitty.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_proper_sleeping(self):
        self.kitty.fed = True
        self.kitty.sleepy = True
        self.kitty.sleep()
        self.assertFalse(self.kitty.sleepy)


if __name__ == "__main__":
    unittest.main()
