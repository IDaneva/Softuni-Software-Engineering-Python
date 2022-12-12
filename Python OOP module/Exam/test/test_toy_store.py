from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_method_with_nonexistent_shelf_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("1", "teddy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_method_with_this_toy_on_shelf_expect_error(self):
        self.toy_store.toy_shelf["A"] = "teddy"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "teddy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_method_when_other_toy_on_shelf_expect_error(self):
        self.toy_store.toy_shelf["A"] = "teddy"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "doll")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_correct_adding_toy_method(self):
        self.toy_store.toy_shelf["A"] = "teddy"
        res = self.toy_store.add_toy("D", "doll")
        self.assertEqual("Toy:doll placed successfully!", res)
        self.assertEqual({"A": "teddy",
                          "B": None,
                          "C": None,
                          "D": "doll",
                          "E": None,
                          "F": None,
                          "G": None}, self.toy_store.toy_shelf)

    def test_remove_toy_method_non_existent_shelf_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("1", "teddy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_method_when_other_toy_on_shelf(self):
        self.toy_store.toy_shelf["A"] = "teddy"
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "T-Rex plush")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_correct_removal_of_toy(self):
        self.toy_store.toy_shelf["A"] = "teddy"
        res = self.toy_store.remove_toy("A", "teddy")
        self.assertEqual("Remove toy:teddy successfully!", res)
        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None}, self.toy_store.toy_shelf)


if __name__ == "__main__":
    unittest.main()
