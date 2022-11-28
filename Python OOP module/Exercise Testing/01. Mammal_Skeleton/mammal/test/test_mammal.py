import unittest
from mammal.project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.animal = Mammal("mrs Vidrason", "otter", "squeak")

    def test_proper_initialization(self):
        self.assertEqual("mrs Vidrason", self.animal.name)
        self.assertEqual("otter", self.animal.type)
        self.assertEqual("squeak", self.animal.sound)
        self.assertEqual("animals", self.animal._Mammal__kingdom)

    def test_get_sound_method(self):
        self.assertEqual("mrs Vidrason makes squeak", self.animal.make_sound())

    def test_get_kingdom_method(self):
        self.assertEqual("animals", self.animal.get_kingdom())

    def test_info_repr_method(self):
        self.assertEqual("mrs Vidrason is of type otter", self.animal.info())


if __name__ == "__main__":
    unittest.main()
