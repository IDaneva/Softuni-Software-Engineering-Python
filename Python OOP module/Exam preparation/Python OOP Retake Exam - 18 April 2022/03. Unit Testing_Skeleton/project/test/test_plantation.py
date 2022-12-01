from project.plantation import Plantation

import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self):
        self.plantation = Plantation(50)

    def test_proper_initialization(self):
        self.assertEqual(50, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_with_incorrect_size_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -10
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_size_setter_with_proper_amount(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_size_setter_with_proper_positive_amount(self):
        self.plantation.size = 15
        self.assertEqual(15, self.plantation.size)

    def test_hire_worker_method_worker_already_hired_expect_error(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_method_worker_not_hired(self):
        result = self.plantation.hire_worker("Pesho")
        self.assertEqual(["Pesho"], self.plantation.workers)
        self.assertEqual("Pesho successfully hired.", result)

    def test_len_method_with_no_plants(self):
        self.assertEqual(0, len(self.plantation))

    def test_len_method_with_added_plants(self):
        self.plantation.plants = {"lilac": "ten", "roses": "eleven"}
        self.assertEqual(9, len(self.plantation))

    def test_planting_method_worker_not_hired(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "rose")
        self.assertEqual("Worker with name Gosho is not hired!", str(ve.exception))

    def test_planting_method_when_plantation_is_full(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"roses": "1"*50}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "roses")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_method_when_worker_is_in_dict_dif_flower(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["roses"]}
        res = self.plantation.planting("Pesho", "violets")
        self.assertEqual({"Pesho": ["roses", "violets"]}, self.plantation.plants)
        self.assertEqual("Pesho planted violets.", res)

    def test_planting_method_when_worker_is_in_dict_same_flower(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["roses"]}
        res = self.plantation.planting("Pesho", "roses")
        self.assertEqual({"Pesho": ["roses", "roses"]}, self.plantation.plants)
        self.assertEqual("Pesho planted roses.", res)

    def test_planting_method_when_worker_is_not_in_dict(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.plants = {"Pesho": ["roses"]}
        res = self.plantation.planting("Gosho", "roses")
        self.assertEqual({"Pesho": ["roses"], "Gosho": ["roses"]}, self.plantation.plants)
        self.assertEqual("Gosho planted it's first roses.", res)

    def test_correct_str_method(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.plants = {"Pesho": ["roses"], "Gosho": ["roses"]}
        self.assertEqual("Plantation size: 50\n"
                         "Pesho, Gosho\n"
                         "Pesho planted: roses\n"
                         "Gosho planted: roses", str(self.plantation))

    def test_correct_repr_method(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.assertEqual("Size: 50\nWorkers: Pesho, Gosho", self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()
