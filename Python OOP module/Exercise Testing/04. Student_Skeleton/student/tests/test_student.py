import unittest
from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student_without_initial_courses = Student("Pesho")
        self.student = Student("Gosho", {"Geology": ["some notes in Geology"]})

    def test_proper_initialization(self):
        self.assertEqual("Gosho", self.student.name)
        self.assertEqual("Pesho", self.student_without_initial_courses.name)
        self.assertEqual({}, self.student_without_initial_courses.courses)
        self.assertEqual({"Geology": ["some notes in Geology"]}, self.student.courses)

    def test_enroll_method_when_course_is_in_courses_dict_and_there_is_no_parameter(self):
        result = self.student.enroll("Geology", ["more notes", "last note for subject"])
        self.assertEqual(["some notes in Geology", "more notes", "last note for subject"], self.student.courses["Geology"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_method_when_course_is_in_courses_dict_and_there_a_third_parameter(self):
        result = self.student.enroll("Geology", ["more notes", "last note for subject"], "Y")
        self.assertEqual(["some notes in Geology", "more notes", "last note for subject"], self.student.courses["Geology"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_method_when_course_is_in_courses_dict_and_there_a_third_negative_parameter(self):
        result = self.student.enroll("Bio", ["more notes", "last note for subject"], "N")
        self.assertEqual([], self.student.courses["Bio"])
        self.assertEqual("Course has been added.", result)

    def test_enroll_method_when_course_should_be_added(self):
        result = self.student_without_initial_courses.enroll("Math", ["1 + 2 = 4", "a^2 + b^2 = c^2"])
        self.assertEqual(["1 + 2 = 4", "a^2 + b^2 = c^2"], self.student_without_initial_courses.courses["Math"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_when_no_notes_should_be_kept(self):
        result = self.student_without_initial_courses.enroll("Music", ["Mozart is great!"], "N")
        self.assertEqual([], self.student_without_initial_courses.courses["Music"])
        self.assertEqual("Course has been added.", result)

    def test_enroll_method_when_notes_should_be_kept(self):
        result = self.student.enroll("Music", ["Mozart is great!"], "Y")
        self.assertEqual(["Mozart is great!"], self.student.courses["Music"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_method_to_existing_course(self):
        result = self.student.add_notes("Geology", "The Earth is flat")
        self.assertEqual(["some notes in Geology", "The Earth is flat"], self.student.courses["Geology"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_method_to_nonexistent_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("History", "Trump was the best president")
        self.assertEqual({"Geology": ["some notes in Geology"]}, self.student.courses)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_is_in_the_dict(self):
        result = self.student.leave_course("Geology")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_method_when_course_is_nonexistent(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_initial_courses.leave_course("Biology")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
