from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Avatar", 2022, 9.7)
        self.other = Movie("Toy Story", 2015, 7.1)

    def test_proper_initialization(self):
        self.assertEqual("Avatar", self.movie.name)
        self.assertEqual(2022, self.movie.year)
        self.assertEqual(9.7, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_wrong_name_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_name_setter_with_proper_name(self):
        self.movie.name = "Avatar 2"
        self.assertEqual("Avatar 2", self.movie.name)

    def test_year_setter_with_incorrect_year_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_year_setter_with_proper_year(self):
        self.movie.year = 1900
        self.assertEqual(1900, self.movie.year)

    def test_add_actor_method_when_actor_is_not_in_cast_yet(self):
        self.movie.add_actor("Scarlet Johansson")
        self.assertEqual(["Scarlet Johansson"], self.movie.actors)

    def test_add_actor_when_there_is_cast_and_actor_isnt_in_it(self):
        self.movie.actors = ["Scarlet Johansson", "Bob", "Jeffrey"]
        self.movie.add_actor("Franklin")
        self.assertEqual(["Scarlet Johansson", "Bob", "Jeffrey", "Franklin"], self.movie.actors)

    def test_add_actor_when_actor_is_in_cast(self):
        self.movie.actors = ["Scarlet Johansson", "Bob", "Jeffrey"]
        res = self.movie.add_actor("Scarlet Johansson")
        self.assertEqual("Scarlet Johansson is already added in the list of actors!", res)

    def test_correct__gt__method(self):
        res = self.movie.__gt__(self.other)
        self.assertEqual('"Avatar" is better than "Toy Story"', res)

    def test_correct__gt__method_with_symbol(self):
        res = self.movie > self.other
        self.assertEqual('"Avatar" is better than "Toy Story"', res)

    def test_correct__gt_method_when_other_is_better(self):
        self.other.rating = 10
        res = self.movie.__gt__(self.other)
        self.assertEqual('"Toy Story" is better than "Avatar"', res)

    def test_correct__gt_method_when_other_is_better_with_symbol(self):
        self.other.rating = 10
        res = self.movie > self.other
        self.assertEqual('"Toy Story" is better than "Avatar"', res)

    def test_correct_repr_method_no_cast(self):
        self.assertEqual("Name: Avatar\n"
                         "Year of Release: 2022\n"
                         "Rating: 9.70\n"
                         "Cast: ", self.movie.__repr__())

    def test_correct_repr_method_with_cast(self):
        self.movie.actors = ["Scarlet Johansson", "Bob", "Jeffrey"]

        self.assertEqual("Name: Avatar\n"
                         "Year of Release: 2022\n"
                         "Rating: 9.70\n"
                         "Cast: Scarlet Johansson, Bob, Jeffrey", self.movie.__repr__())


if __name__ == "__main__":
    unittest.main()
