import unittest
from project_python_oop_exam_christmas_pastry_shop.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Patlak")                                        # create student with empty courses
        self.student_courses = Student("Kiuftak", {"math": ["some note"]})      # create student with course 'math

    def test_correct_init(self):                                # test correct initialization of student
        self.assertEqual("Patlak", self.student.name)           # compare student name with added name
        self.assertEqual({}, self.student.courses)              # check if empty dictionary is added
        self.assertEqual({"math": ["some note"]}, self.student_courses.courses)   # check if course and notes are added

    def test_enroll_add_notes_to_existing_course(self):             # test enroll method to add notes to existing course
        result = self.student_courses.enroll("math", ["second note"])       # Act: add note to the existing course
        self.assertEqual("second note", self.student_courses.courses["math"][1])    # check if added note exist in dict
        self.assertEqual("Course already added. Notes have been updated.", result)  # test expected message as result

    # check add notes to not existing course with no add_course_notes
    def test_add_notes_to_not_existing_course_without_third_param(self):
        # using empty student 'Patlak' to add course and notes
        result = self.student.enroll("math", ["math note"])         # Act: try to add note to not existing course
        self.assertEqual("Course and course notes have been added.", result)  # compare expected message with result msg

    # check add notes to not existing course with add_course_notes
    def test_add_notes_to_not_existing_course_with_third_param(self):
        # using empty student 'Patlak' to add course and add_course_notes
        result = self.student.enroll("math", ["math note"], "Y")    # Act: try to add add_course_notes to not existing course with
        self.assertEqual("Course and course notes have been added.", result)  # compare expected message with result msg

    def test_add_new_course_without_notes(self):        # try add course without notes
        # using empty student 'Patlak' to add course and add_course_notes
        result = self.student.enroll("math", ["math note"], "N")    # Act: add new course without notes
        self.assertEqual(0, len(self.student.courses["math"]))      # Assert: check len of courses of the student
        self.assertEqual("Course has been added.", result)          # Assert: compare expected message with result msg

    def test_add_notes(self):   # test add notes
        result = self.student_courses.add_notes("math", "second note")  # Act: add second note to existing course, Arrange: result
        self.assertEqual(2, len(self.student_courses.courses["math"]))  # Assert: check len of notes in the existing course
        self.assertEqual("Notes have been updated", result)             # Assert: compare expected message with result msg
        with self.assertRaises(Exception) as ex:                        # Arrange: raise exception
            self.student.add_notes("geography", "blabla")               # Act: try to add note to not existing course
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))  # Assert: compare expected message with result msg

    def test_leave_course(self):                                # test leave/remove course
        result = self.student_courses.leave_course("math")      # Act: leave course, Arrange: result
        self.assertEqual({}, self.student.courses)              # Assert: check if dictionary is empty
        self.assertEqual("Course has been removed", result)     # Assert: compare expected message with result msg
        with self.assertRaises(Exception) as ex:                # Arrange: raise exception
            self.student.leave_course("geography")              # Act: try to leave not existing course
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))  # Assert: compare expected message with result msg


if __name__ == "__main__":
    unittest.main()
