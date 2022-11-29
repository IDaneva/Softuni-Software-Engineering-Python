from project.team import Team
import unittest


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Celtics")
        self.people = {"Gogo": 18, "Sashko": 10, "Simo": 5, "Kircho": 7}
        self.other = Team("Mercedes")

    def test_proper_initialization(self):
        self.assertEqual("Celtics", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_wrong_name_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "123"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_name_setter_name_with_int_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "ABC0"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_name_setter_with_proper_name(self):
        self.team.name = "Boston"
        self.assertEqual("Boston", self.team.name)

    def test_add_member_method_no_members_before(self):
        res = self.team.add_member(**{"Niki": 20})
        self.assertEqual({"Niki": 20}, self.team.members)
        self.assertEqual("Successfully added: Niki", res)

    def test_add_member_method_with_members_before(self):
        self.team.members = self.people
        res = self.team.add_member(**{"Niki": 20})
        self.assertEqual({'Gogo': 18, 'Kircho': 7, 'Niki': 20, 'Sashko': 10, 'Simo': 5}, self.team.members)
        self.assertEqual("Successfully added: Niki", res)

    def test_add_member_with_multiple_new_ones(self):
        self.team.members = self.people
        res = self.team.add_member(**{"Niki": 20, "Nina": 19})
        self.assertEqual({'Gogo': 18, 'Kircho': 7, 'Niki': 20, 'Nina': 19, 'Sashko': 10, 'Simo': 5}, self.team.members)
        self.assertEqual("Successfully added: Niki, Nina", res)

    def test_add_member_method_with_already_added_member(self):
        self.team.members = self.people
        res = self.team.add_member(**{"Gogo": 20, "Nina": 19})
        self.assertEqual({'Gogo': 18, 'Kircho': 7, 'Nina': 19, 'Sashko': 10, 'Simo': 5}, self.team.members)
        self.assertEqual("Successfully added: Nina", res)

    def test_add_member_method_with_already_added_members(self):
        self.team.members = self.people
        res = self.team.add_member(**{"Gogo": 20, "Kircho": 19})
        self.assertEqual({'Gogo': 18, 'Kircho': 7, 'Sashko': 10, 'Simo': 5}, self.team.members)
        self.assertEqual("Successfully added: ", res)

    def test_remove_member_method_with_no_members(self):
        res = self.team.remove_member("Pesho")
        self.assertEqual("Member with name Pesho does not exist", res)

    def test_remove_member_with_members_but_given_one_doesnt_exist(self):
        self.team.members = self.people
        res = self.team.remove_member("Pesho")
        self.assertEqual("Member with name Pesho does not exist", res)

    def test_remove_member_when_member_exists(self):
        self.team.members = self.people
        res = self.team.remove_member("Simo")
        self.assertEqual("Member Simo removed", res)
        self.assertEqual({"Gogo": 18, "Sashko": 10, "Kircho": 7}, self.team.members)

    def test_correct_gt_method_when_no_team_has_members(self):
        self.assertEqual(False, self.team.__gt__(self.other))

    def test_correct_gt_method_when_no_team_has_members_with_symbols(self):
        self.assertEqual(False, self.team > self.other)

    def test_correct_gt_method_with_team_members(self):
        self.team.members = self.people
        self.assertEqual(True, self.team.__gt__(self.other))

    def test_correct_gt_method_with_team_members_with_symbols(self):
        self.team.members = self.people
        self.assertEqual(True, self.team > self.other)

    def test_correct_gt_method_with_other_members(self):
        self.other.members = self.people
        self.assertEqual(False, self.team.__gt__(self.other))

    def test_correct_gt_method_with_other_members_with_symbols(self):
        self.other.members = self.people
        self.assertEqual(False, self.team > self.other)

    def test_len_method_with_no_members(self):
        self.assertEqual(0, len(self.team))

    def test_len_method_with_members(self):
        self.team.members = self.people
        self.assertEqual(4, len(self.team))

    def test_add_method(self):
        new_team = self.team.__add__(self.other)
        self.assertEqual("CelticsMercedes", new_team.name)
        self.assertEqual({}, new_team.members)

    def test_add_method_with_members(self):
        self.team.members = self.people
        new_team = self.team.__add__(self.other)
        self.assertEqual("CelticsMercedes", new_team.name)
        self.assertEqual({"Gogo": 18, "Sashko": 10, "Simo": 5, "Kircho": 7}, new_team.members)

    def test_add_method_with_members_of_both_teams(self):
        self.team.members = self.people
        self.other.members = {"Niki": 20}
        new_team = self.team.__add__(self.other)
        self.assertEqual("CelticsMercedes", new_team.name)
        self.assertEqual({"Gogo": 18, "Sashko": 10, "Simo": 5, "Kircho": 7, "Niki": 20}, new_team.members)

    def test_correct_str_method_with_no_members(self):
        res = str(self.team)
        self.assertEqual("Team name: Celtics", res)

    def test_correct_str_method_with_members(self):
        self.team.members = self.people
        res = str(self.team)
        self.assertEqual("Team name: Celtics\n"
                         "Member: Gogo - 18-years old\n"
                         "Member: Sashko - 10-years old\n"
                         "Member: Kircho - 7-years old\n"
                         "Member: Simo - 5-years old", res)


if __name__ == "__main__":
    unittest.main()
