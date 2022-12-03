from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("Sofia")

    def test_correct_initialization(self):
        self.assertEqual("Sofia", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_with_wrong_name_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_name_setter_with_proper_name(self):
        self.library.name = "Cambodia"
        self.assertEqual("Cambodia", self.library.name)

    def test_add_book_method_when_author_and_book_arent_in_library_no_other_authors(self):
        self.library.add_book("JK Rowling", "Harry Potter 1")
        self.assertEqual({"JK Rowling": ["Harry Potter 1"]}, self.library.books_by_authors)

    def test_add_book_method_when_author_and_book_arent_in_library_with_other_authors(self):
        self.library.books_by_authors = {"Arthur K Doil": ["Sherlok Holmes"]}
        self.library.add_book("JK Rowling", "Harry Potter 1")
        self.assertEqual({"Arthur K Doil": ["Sherlok Holmes"], "JK Rowling": ["Harry Potter 1"]}, self.library.books_by_authors)

    def test_add_book_method_when_author_is_but_book_isnt_in_library(self):
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter"]}
        self.library.add_book("JK Rowling", "Harry Potter 1")
        self.assertEqual({"JK Rowling": ["Harry Potter", "Harry Potter 1"]}, self.library.books_by_authors)

    def test_add_book_method_when_author_is_but_book_isnt_in_library_multiple_authors(self):
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter"], "Arthur K Doil": ["Sherlok Holmes"]}
        self.library.add_book("JK Rowling", "Harry Potter 1")
        self.assertEqual({"JK Rowling": ["Harry Potter", "Harry Potter 1"], "Arthur K Doil": ["Sherlok Holmes"]}, self.library.books_by_authors)

    def test_add_book_method_when_both_are_in_library(self):
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter"], "Arthur K Doil": ["Sherlok Holmes"]}
        self.library.add_book("JK Rowling", "Harry Potter")
        self.assertEqual({"JK Rowling": ["Harry Potter"], "Arthur K Doil": ["Sherlok Holmes"]}, self.library.books_by_authors)

    def test_add_reader_method_when_no_readers(self):
        self.library.add_reader("Kiko")
        self.assertEqual({"Kiko": []}, self.library.readers)

    def test_add_reader_method_when_there_are_readers(self):
        self.library.readers = {"Sami": [], "Nino": []}
        self.library.add_reader("Kiko")
        self.assertEqual({"Sami": [], "Nino": [], "Kiko": []}, self.library.readers)

    def test_add_reader_method_when_reader_is_registered(self):
        self.library.readers = {"Sami": [], "Nino": []}
        res = self.library.add_reader("Sami")
        self.assertEqual("Sami is already registered in the Sofia library.", res)
        self.assertEqual({"Sami": [], "Nino": []}, self.library.readers)

    def test_rent_book_method_when_reader_isnt_registered(self):
        self.library.readers = {"Sami": [], "Nino": []}
        res = self.library.rent_book("Kiko", "JK Rowling", "Harry Potter")
        self.assertEqual("Kiko is not registered in the Sofia Library.", res)

    def test_rent_book_method_when_author_isnt_available(self):
        self.library.readers = {"Sami": [], "Nino": []}
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter"]}
        res = self.library.rent_book("Sami", "Arthur K Doil", "Sherlok Holmes")
        self.assertEqual("Sofia Library does not have any Arthur K Doil's books.", res)

    def test_rent_book_method_when_book_title_isnt_available(self):
        self.library.readers = {"Sami": [], "Nino": []}
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter"]}
        res = self.library.rent_book("Sami", "JK Rowling", "Harry Potter 2")
        self.assertEqual('Sofia Library does not have JK Rowling\'s "Harry Potter 2".', res)

    def test_rent_book_method_when_all_are_available(self):
        self.library.readers = {"Sami": [], "Nino": []}
        self.library.books_by_authors = {"JK Rowling": ["Harry Potter", "Harry Potter 1", "Harry Potter 2"], "Arthur K Doil": ["Sherlok Holmes"]}
        res = self.library.rent_book("Sami", "JK Rowling", "Harry Potter 1")
        self.assertEqual({"Nino": [], "Sami": [{"JK Rowling": "Harry Potter 1"}]}, self.library.readers)
        self.assertEqual({"JK Rowling": ["Harry Potter", "Harry Potter 2"], "Arthur K Doil": ["Sherlok Holmes"]}, self.library.books_by_authors)


if __name__ == "__main__":
    unittest.main()
