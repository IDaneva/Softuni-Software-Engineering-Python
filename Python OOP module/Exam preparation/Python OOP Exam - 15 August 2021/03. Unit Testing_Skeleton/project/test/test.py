from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("MaxiPet")

    def test_initialization(self):
        self.assertEqual("MaxiPet", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_method_when_low_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("cat food", -10)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_method_when_zero_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("cat food", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_method_when_food_is_not_in_petshop(self):
        self.pet_shop.food = {"cat food": 500}
        res = self.pet_shop.add_food("dog food", 1000)
        self.assertEqual({"cat food": 500, "dog food": 1000}, self.pet_shop.food)
        self.assertEqual("Successfully added 1000.00 grams of dog food.", res)

    def test_add_food_method_when_food_is_in_petshop(self):
        self.pet_shop.food = {"cat food": 500}
        res = self.pet_shop.add_food("cat food", 1000)
        self.assertEqual({"cat food": 1500}, self.pet_shop.food)
        self.assertEqual("Successfully added 1000.00 grams of cat food.", res)

    def test_add_pet_method_when_pet_is_in_pet_shop(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Rex")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_when_pet_isnt_in_shop(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        res = self.pet_shop.add_pet("Nino")
        self.assertEqual(["Rex", "Maggy", "Nino"], self.pet_shop.pets)
        self.assertEqual("Successfully added Nino.", res)

    def test_feed_pet_when_pet_isnt_in_shop(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("salmon", "Remi")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_food_isnt_in_shop(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        self.pet_shop.food = {"cat food": 90}
        res = self.pet_shop.feed_pet("salmon", "Rex")
        self.assertEqual("You do not have salmon", res)

    def test_feed_pet_when_food_isnt_enough(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        self.pet_shop.food = {"cat food": 90}
        res = self.pet_shop.feed_pet("cat food", "Rex")
        self.assertEqual("Adding food...", res)
        self.assertEqual({"cat food": 1090}, self.pet_shop.food)

    def test_feed_pet_when_everything_is_fine(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        self.pet_shop.food = {"cat food": 1000}
        res = self.pet_shop.feed_pet("cat food", "Rex")
        self.assertEqual("Rex was successfully fed", res)
        self.assertEqual({"cat food": 900}, self.pet_shop.food)

    def test_correct_repr_method(self):
        self.pet_shop.pets = ["Rex", "Maggy"]
        self.assertEqual("Shop MaxiPet:\n"
                         "Pets: Rex, Maggy", self.pet_shop.__repr__())


if __name__ == "__main__":
    unittest.main()
