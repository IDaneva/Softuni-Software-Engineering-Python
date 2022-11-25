import unittest

from Testing.codes.car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("VW", "Golf", 5.5, 50)

    def test_initialization(self):
        self.assertEqual("VW", self.car.make)
        self.assertEqual("Golf", self.car.model)
        self.assertEqual(5.5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_with_wrong_manufacturer(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter_with_proper_manufacturer(self):
        self.car.make = "BMW"
        self.assertEqual("BMW", self.car.make)

    def test_model_setter_with_wrong_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_setter_with_proper_model(self):
        self.car.model = "i3"
        self.assertEqual("i3", self.car.model)

    def test_fuel_consumption_setter_with_invalid_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -10
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_with_proper_consumption(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_fuel_capacity_setter_with_invalid_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -10
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_with_proper_capacity(self):
        self.car.fuel_capacity = 75
        self.assertEqual(75, self.car.fuel_capacity)

    def test_fuel_amount_setter_with_invalid_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_setter_with_proper_amount(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_method_with_invalid_amount_expect_exception_rise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_proper_amount_expect_fuel_amount_increase(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_method_with_amount_bigger_than_the_capacity(self):
        self.car.refuel(210)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_method_with_not_enough_fuel_expect_exception_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_with_some_fuel_expect_fuel_decrease(self):
        self.car.fuel_amount = 50
        self.car.drive(50)
        self.assertEqual(47.25, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()
