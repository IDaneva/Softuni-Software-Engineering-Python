import unittest

from Testing.codes.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList(1, "70", 55.5, 6, "abc", 10)

    def test_get_data_method(self):
        self.assertEqual(self.list._IntegerList__data, self.list.get_data())

    def test_proper_initialization(self):
        self.assertEqual([1, 6, 10], self.list.get_data())

    def test_adding_elements_when_non_integer_is_given(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("50")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_method_when_integer_value_is_passed(self):
        self.list.add(5)
        self.assertEqual([1, 6, 10, 5], self.list.get_data())

    def test_remove_index_method_when_invalid_index_is_passed(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_method_with_proper_index(self):
        self.assertEqual(1, self.list.remove_index(0))
        self.assertEqual([6, 10], self.list.get_data())

    def test_get_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_with_proper_index(self):
        self.assertEqual(1, self.list.get(0))

    def test_insert_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(4, 0)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_with_invalid_type(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "2")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_with_proper_index_and_value(self):
        self.list.insert(0, 0)
        self.assertEqual([0, 1, 6, 10], self.list.get_data())

    def test_get_biggest_method(self):
        self.assertEqual(10, self.list.get_biggest())

    def test_get_index_method(self):
        self.assertEqual(0, self.list.get_index(1))


if __name__ == "__main__":
    unittest.main()
