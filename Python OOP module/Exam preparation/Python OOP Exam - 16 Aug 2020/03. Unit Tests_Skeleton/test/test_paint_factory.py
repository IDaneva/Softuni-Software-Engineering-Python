from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Fabrika 126", 100)

    def test_initialization(self):
        self.assertEqual("Fabrika 126", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_can_add_method_when_available_capacity(self):
        self.paint_factory.ingredients = {"red paint": 60}
        self.assertEqual(True, self.paint_factory.can_add(30))

    def test_can_add_method_when_no_capacity(self):
        self.paint_factory.ingredients = {"red paint": 60}
        self.assertEqual(False, self.paint_factory.can_add(50))

    def test_repr_method_when_no_ingredients(self):
        self.assertEqual("Factory name: Fabrika 126 with capacity 100.\n", self.paint_factory.__repr__())

    def test_repr_method_with_ingredients(self):
        self.paint_factory.ingredients = {"red paint": 60, "blue paint": 10, "green paint": 20}
        self.assertEqual("Factory name: Fabrika 126 with capacity 100.\n"
                         "red paint: 60\n"
                         "blue paint: 10\n"
                         "green paint: 20\n", self.paint_factory.__repr__())

    def test_add_ingredient_when_product_type_not_valid(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("black", 100)

        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))

    def test_add_ingredient_when_valid_product_type_no_space(self):
        self.paint_factory.ingredients = {"red": 60, "blue": 10, "green": 20}
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("yellow", 20)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_when_available_space_ingredient_in_ingredients(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        self.paint_factory.add_ingredient("blue", 20)
        self.assertEqual({"red": 50, "blue": 30, "green": 20}, self.paint_factory.ingredients)
        self.assertEqual(3, len(self.paint_factory.ingredients))
        self.assertEqual(30, self.paint_factory.ingredients["blue"])

    def test_add_ingredient_when_available_space_ingredient_not_in_ingredients(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        self.paint_factory.add_ingredient("white", 20)
        self.assertEqual({"red": 50, "blue": 10, "green": 20, "white": 20}, self.paint_factory.ingredients)
        self.assertEqual(4, len(self.paint_factory.ingredients))
        self.assertEqual(20, self.paint_factory.ingredients["white"])

    def test_remove_ingredient_when_ingredient_not_in_factory(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_when_given_negative_quantity(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("red", 60)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_with_proper_input(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        self.paint_factory.remove_ingredient("red", 20)
        self.assertEqual({"red": 30, "blue": 10, "green": 20}, self.paint_factory.ingredients)
        self.assertEqual(3, len(self.paint_factory.ingredients))
        self.assertEqual(30, self.paint_factory.ingredients["red"])

    def test_property_products(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_property_products_with_added_products(self):
        self.paint_factory.ingredients = {"red": 50, "blue": 10, "green": 20}
        self.assertEqual({"red": 50, "blue": 10, "green": 20}, self.paint_factory.products)


if __name__ == "__main__":
    unittest.main()
