from project.student_report_card import StudentReportCard
import unittest


class TestStudentReportCart(unittest.TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Ivana", 12)

    def test_initialization(self):
        self.assertEqual("Ivana", self.student_report_card.student_name)
        self.assertEqual(12, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_grades_setter(self):
        self.student_report_card.grades_by_subject = {"math": [4.5, 2, 6], "chemistry": [2, 3, 2]}
        self.assertEqual({"math": [4.5, 2, 6], "chemistry": [2, 3, 2]}, self.student_report_card.grades_by_subject)

    def test_name_setter_wrong_name_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_name_setter_proper_name(self):
        self.student_report_card.student_name = "Niki"
        self.assertEqual("Niki", self.student_report_card.student_name)

    def test_year_setter_wrong_year_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 2019
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_year_setter_negative_year_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 2019
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_year_setter_with_proper_year(self):
        self.student_report_card.school_year = 11
        self.assertEqual(11, self.student_report_card.school_year)

    def test_add_grade_when_no_subject(self):
        self.student_report_card.add_grade("math", 6.00)
        self.assertEqual({"math": [6.00]}, self.student_report_card.grades_by_subject)

    def test_add_grade_when_subject_not_in_grades(self):
        self.student_report_card.grades_by_subject = {"math": [4.50, 2.00, 6.00], "history": [3.00, 6.00, 9.00]}
        self.student_report_card.add_grade("biology", 5.00)
        self.assertEqual({"math": [4.50, 2.00, 6], "history": [3.00, 6.00, 9.00], "biology": [5.00]}, self.student_report_card.grades_by_subject)

    def test_add_grade_when_subject_in_grades(self):
        self.student_report_card.grades_by_subject = {"math": [4.50, 2.00, 6.00]}
        self.student_report_card.add_grade("math", 5.42)
        self.assertEqual({"math": [4.50, 2.00, 6.00, 5.42]}, self.student_report_card.grades_by_subject)

    def test_add_grade_when_subject_in_grades_grade_is_already_used(self):
        self.student_report_card.grades_by_subject = {"math": [4.50, 2.00, 6.00]}
        self.student_report_card.add_grade("math", 20.00)
        self.assertEqual({"math": [4.50, 2.00, 6.00, 20.00]}, self.student_report_card.grades_by_subject)

    def test_successful_average_grade_by_subject(self):
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Fund", 6.00)
        result = self.student_report_card.average_grade_by_subject()

        self.assertEqual([6.0, 6.0], self.student_report_card.grades_by_subject["P - Basic"])
        self.assertEqual([6.0], self.student_report_card.grades_by_subject["P - Fund"])
        self.assertEqual(1, len(self.student_report_card.grades_by_subject["P - Fund"]))
        self.assertEqual("P - Basic: 6.00\n"
                         "P - Fund: 6.00", result)

    def test_average_grade_when_no_subjects_and_grades(self):
        res = self.student_report_card.average_grade_by_subject()
        self.assertEqual("", res)

    def test_average_grade_method_when_subjects_no_grades(self):
        self.student_report_card.grades_by_subject = {"math": [], "history": []}
        with self.assertRaises(ZeroDivisionError) as ze:
            self.student_report_card.average_grade_by_subject()
        self.assertEqual("division by zero", str(ze.exception))

    def test_average_grade_method_when_some_grades(self):
        self.student_report_card.grades_by_subject = {"math": [5, 6], "history": []}
        with self.assertRaises(ZeroDivisionError) as ze:
            self.student_report_card.average_grade_by_subject()
        self.assertEqual("division by zero", str(ze.exception))

    def test_average_grade_with_grades(self):
        self.student_report_card.grades_by_subject = {"math": [4.50, 2.00, 6.00], "chemistry": [2, 3, 2], "biology": [5]}
        res = self.student_report_card.average_grade_by_subject()
        self.assertEqual("math: 4.17\n"
                         "chemistry: 2.33\n"
                         "biology: 5.00", res)

    def test_average_grade_for_all_subjects_when_available_grades(self):
        self.student_report_card.grades_by_subject = {"math": [4.5, 2, 6], "chemistry": [2, 3, 2], "biology": [5]}
        res = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 3.50", res)

    def test_average_grade_for_all_method_when_subjects_no_grades(self):
        self.student_report_card.grades_by_subject = {"math": [], "history": []}
        with self.assertRaises(ZeroDivisionError) as ze:
            self.student_report_card.average_grade_by_subject()
        self.assertEqual("division by zero", str(ze.exception))

    def test_correct_repr_method(self):
        self.student_report_card.grades_by_subject = {"math": [4.5, 2, 6], "chemistry": [2, 3, 2], "biology": [5]}
        self.assertEqual("Name: Ivana\n"
                         "Year: 12\n"
                         "----------\n"
                         "math: 4.17\n"
                         "chemistry: 2.33\n"
                         "biology: 5.00\n"
                         "----------\n"
                         "Average Grade: 3.50", self.student_report_card.__repr__())


if __name__ == "__main__":
    unittest.main()
