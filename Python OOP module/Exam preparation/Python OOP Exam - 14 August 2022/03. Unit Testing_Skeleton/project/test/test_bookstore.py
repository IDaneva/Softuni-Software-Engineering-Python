from project.bookstore import Bookstore

import unittest


class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.bookstore = Bookstore(20)

    def test_proper_initialization(self):
        self.assertEqual(20, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_setter_wrong_amount_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -15

        self.assertEqual("Books limit of -15 is not valid", str(ve.exception))

    def test_book_limit_setter_zero_amount_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_setter_with_proper_amount(self):
        self.bookstore.books_limit = 50
        self.assertEqual(50, self.bookstore.books_limit)

    def test_len_method_returns_number_of_copies(self):
        self.assertEqual(0, len(self.bookstore))

    def test_len_method_with_added_books(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20,
                                                               "Peter Pan": 30,
                                                               "Criminals": 40}
        self.assertEqual(100, len(self.bookstore))

    def test_receive_book_method_with_too_many_copies_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Matilda", 30)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_with_reached_limit_already(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 20}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Matilda", 30)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_with_too_many_copies_with_some_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Matilda", 30)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_with_proper_amount_of_copies(self):
        result = self.bookstore.receive_book("Matilda", 5)
        self.assertEqual({"Matilda": 5}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, len(self.bookstore))
        self.assertEqual("5 copies of Matilda are available in the bookstore.", result)

    def test_receive_book_method_with_reaching_the_limit(self):
        self.bookstore.availability_in_store_by_book_titles = {"Some books": 18}
        result = self.bookstore.receive_book("Matilda", 2)
        self.assertEqual({"Some books": 18, "Matilda": 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(20, len(self.bookstore))
        self.assertEqual("2 copies of Matilda are available in the bookstore.", result)

    def test_receive_book_method_when_title_is_available(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 5,
                                                               "Matilda": 5}

        result = self.bookstore.receive_book("Matilda", 5)
        self.assertEqual({"Harry Potter": 5, "Matilda": 10}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(15, len(self.bookstore))
        self.assertEqual("10 copies of Matilda are available in the bookstore.", result)

    def test_sell_book_method_with_unavailable_book_title_expect_error(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20,
                                                               "Peter Pan": 30,
                                                               "Criminals": 40}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Programming for dummies", 10)
        self.assertEqual("Book Programming for dummies doesn't exist!", str(ex.exception))

    def test_sell_book_with_no_books(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Harry Potter", 20)
        self.assertEqual("Book Harry Potter doesn't exist!", str(ex.exception))

    def test_sell_book_method_with_not_enough_quantity_expect_error(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20,
                                                               "Peter Pan": 30,
                                                               "Criminals": 40}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Harry Potter", 20)
        self.assertEqual("Harry Potter has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_method_when_it_can_be_sold_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20}
        result = self.bookstore.sell_book("Matilda", 5)
        self.assertEqual({"Harry Potter": 10, "Matilda": 15}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual("Sold 5 copies of Matilda", result)

    def test_sell_all_books_with_that_title_expect_0_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20}
        result = self.bookstore.sell_book("Matilda", 20)
        self.assertEqual({"Harry Potter": 10, "Matilda": 0}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(20, self.bookstore.total_sold_books)
        self.assertEqual("Sold 20 copies of Matilda", result)

    def test_correct__str_method(self):
        self.bookstore.books_limit = 100
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 10,
                                                               "Matilda": 20,
                                                               "Peter Pan": 30,
                                                               "Criminals": 40}
        self.bookstore.sell_book("Matilda", 5)
        result = "Total sold books: 5\n" \
                 "Current availability: 95\n" \
                 " - Harry Potter: 10 copies\n" \
                 " - Matilda: 15 copies\n" \
                 " - Peter Pan: 30 copies\n" \
                 " - Criminals: 40 copies"
        self.assertEqual(result, str(self.bookstore))


if __name__ == "__main__":
    unittest.main()
