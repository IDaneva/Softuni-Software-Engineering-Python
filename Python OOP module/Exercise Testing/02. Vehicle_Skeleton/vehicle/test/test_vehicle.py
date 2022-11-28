import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(50, 90)

    def test_class_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(self.car.capacity, self.car.fuel)
        self.assertEqual(90, self.car.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive_method_without_the_needed_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_with_needed_fuel_expect_to_be_correct(self):
        self.car.drive(5)
        self.assertEqual(43.75, self.car.fuel)

    def test_refuel_method_with_too_much_fuel_expect_exception(self):
        self.car.fuel = 45
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_when_proper_amount_is_given(self):
        self.car.fuel = 45
        self.car.refuel(5)
        self.assertEqual(50, self.car.fuel)

    def test_string_method(self):
        result = str(self.car)
        expected = "The vehicle has 90 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
