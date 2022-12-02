from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("MaxiPet", 50_000)
        self.other = ShoppingCart("PetMall", 10)

    def test_proper_initialization(self):
        self.assertEqual("MaxiPet", self.shopping_cart.shop_name)
        self.assertEqual(50_000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_setter_with_incorrect_name(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "0123"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_setter_with_correct_name(self):
        self.shopping_cart.shop_name = "TheFamily"
        self.assertEqual("TheFamily", self.shopping_cart.shop_name)

    def test_add_to_cart_method_with_too_high_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("dog toys", 111.11)
        self.assertEqual("Product dog toys cost too much!", str(ve.exception))

    def test_add_to_cart_method_with_normal_price(self):
        self.shopping_cart.products = {"cat food": 50}
        result = self.shopping_cart.add_to_cart("dog toys", 89.11)
        self.assertEqual({"dog toys": 89.11, "cat food": 50}, self.shopping_cart.products)
        self.assertEqual("dog toys product was successfully added to the cart!", result)

    def test_remove_from_cart_method_with_nonexistent_product(self):
        self.shopping_cart.products = {"dog toys": 89.11, "cat food": 100}
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("kitty litter")
        self.assertEqual("No product with name kitty litter in the cart!", str(ve.exception))

    def test_remove_from_cart_method_with_existing_product(self):
        self.shopping_cart.products = {"dog toys": 89.11, "cat food": 100}
        result = self.shopping_cart.remove_from_cart("dog toys")
        self.assertEqual({"cat food": 100}, self.shopping_cart.products)
        self.assertEqual("Product dog toys was successfully removed from the cart!", result)

    def test_adding_another_shopping_cart_from_dif_shop_no_products(self):
        new_shopping_cart = self.shopping_cart.__add__(self.other)
        self.assertEqual("MaxiPetPetMall", new_shopping_cart.shop_name)
        self.assertEqual(50_010, new_shopping_cart.budget)
        self.assertEqual({}, new_shopping_cart.products)

    def test_adding_another_shopping_cart_from_dif_shop_with_products(self):
        self.shopping_cart.products = {"dog toys": 89.11}
        self.other.products = {"kitty litter": 50}
        new_shopping_cart = self.shopping_cart.__add__(self.other)
        self.assertEqual("MaxiPetPetMall", new_shopping_cart.shop_name)
        self.assertEqual(50_010, new_shopping_cart.budget)
        self.assertEqual({"dog toys": 89.11, "kitty litter": 50}, new_shopping_cart.products)

    def test_buying_method_without_needed_money(self):
        self.shopping_cart.products = {"dog toys": 89.11, "more toys": 5}
        self.shopping_cart.budget = 89.11
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 5.00lv!", str(ve.exception))

    def test_buying_method_without_needed_money_formatting(self):
        self.shopping_cart.products = {"dog toys": 89, "more toys": 5}
        self.shopping_cart.budget = 89
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 5.00lv!", str(ve.exception))

    def test_buying_method_with_enough_money(self):
        self.shopping_cart.products = {"dog toys": 89.11, "more toys": 5}
        self.shopping_cart.budget = 94.11
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 94.11lv.", result)

    def test_buying_method_formatting(self):
        self.shopping_cart.products = {"dog toys": 89, "more toys": 5}
        self.shopping_cart.budget = 94
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 94.00lv.", result)

    def test_buying_method_with_no_products(self):
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 0.00lv.", result)


if __name__ == "__main__":
    unittest.main()
