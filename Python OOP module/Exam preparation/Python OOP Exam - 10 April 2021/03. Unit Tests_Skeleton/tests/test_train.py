from project.train.train import Train
import unittest


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train("za Sofia", 100)

    def test_initialization(self):
        self.assertEqual("za Sofia", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_when_train_is_full(self):
        self.train.capacity = 3
        self.train.passengers = ["Niki", "Vladi", "Simo"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Pesho")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_when_passenger_is_added(self):
        self.train.capacity = 5
        self.train.passengers = ["Niki", "Vladi", "Simo"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Vladi")
        self.assertEqual("Passenger Vladi Exists", str(ve.exception))

    def test_add_when_passenger_should_be_added(self):
        self.train.capacity = 5
        self.train.passengers = ["Niki", "Vladi", "Simo"]
        res = self.train.add("Pesho")
        self.assertEqual("Added passenger Pesho", res)

    def test_remove_passenger_when_passenger_is_missing(self):
        self.train.passengers = ["Niki", "Vladi", "Simo"]
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Pesho")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_when_passenger_is_in_train(self):
        self.train.passengers = ["Niki", "Vladi", "Simo"]
        res = self.train.remove("Niki")
        self.assertEqual("Removed Niki", res)
        self.assertEqual(["Vladi", "Simo"], self.train.passengers)


if __name__ == "__main__":
    unittest.main()
