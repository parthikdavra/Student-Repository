"""
this code has test cases for the compare tables of student, instructor and majors Repository
Name: Parthik Davra
CWID: 10469593
"""
# all imports
import os
import unittest
from Student_Repository_Parthik_Davra import Repository, Student, Instructor, Major
import sqlite3


class MajorTest(unittest.TestCase):
    """ test cases for Major calss methods in Repository """

    def test_majors_table_data(self) -> None:
        """ verify that all data in Majors table is correct """

        self.repository: Repository = Repository(
            "D:\CS-810\HW11", "D:\CS-810\HW11\Homework11.db")

        final_result: List[str] = [majors.majors_detail()
                                   for majors in self.repository._majors.values()]
        result_expected: List[str] = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                                      ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]
        wrong_result: List[str] = []
        majors_table: PrettyTable = self.repository.majors_pretty_table()

        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)


class StudentTest(unittest.TestCase):
    """ test cases for Student calss methods in Repository """

    def test_student_table_data(self) -> None:
        """ verify that all data in Student table is correct """

        self.repository: Repository = Repository("D:\CS-810\HW11", "D:\CS-810\HW11\Homework11.db"
                                                 )
        final_result: List[str] = [student_name.students_details()
                                   for student_cwid, student_name in self.repository._students.items()]
        result_expected: List[str] = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                                      ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], [
                                          'SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2.0],
                                      ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'],
                                       ['SSW 540'], ['CS 501', 'CS 546'], 4.0],
                                      ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]
        wrong_result: List[str] = []
        student_table: PrettyTable = self.repository.student_pretty_table()

        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)


class InstuctorTest(unittest.TestCase):
    """ test cases for Instructor calss methods in Repository """

    def test_instructor_table_data(self) -> None:
        """ verify that all data in Instuctor table is correct """

        self.repository: Repository = Repository("D:\CS-810\HW11", "D:\CS-810\HW11\Homework11.db"
                                                 )
        final_result: List[str] = [tuple(instructor_detail) for instructor_data in self.repository._instructors.values(
        ) for instructor_detail in instructor_data.instructors_details()]
        result_expected: List[str] = [('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                                      ('98763', 'Rowland, J',
                                       'SFEN', 'SSW 810', 4),
                                      ('98763', 'Rowland, J',
                                       'SFEN', 'SSW 555', 1),
                                      ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                                      ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                                      ('98762', 'Hawking, S', 'CS', 'CS 570', 1)]

        wrong_result: List[str] = []
        instructor_table: PrettyTable = self.repository.instructor_pretty_table()
        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)

    def test_students_grade_table_data(self) -> None:
        """ verify that all data in Grade table is correct """
        self.repository: Repository = Repository("D:\CS-810\HW11", "D:\CS-810\HW11\Homework11.db"
                                                 )
        final_result: List[str] = []
        db: sqlite3.Connection = sqlite3.connect(
            "D:\CS-810\HW11\Homework11.db")
        for data_row in db.execute(
                "SELECT student.Name, student.CWID, grade.Course,  grade.Grade, instructor.Name FROM students student, grades grade,  instructors instructor WHERE student.CWID = StudentCWID AND InstructorCWID = instructor.CWID ORDER BY student.Name"):
            final_result.append(data_row)
        result_expected = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                    ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                    ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                    ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                    ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                    ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                    ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                    ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                    ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]

        grade_table: PrettyTable = self.repository.student_grades_table_db(
            "D:\CS-810\HW11\Homework11.db")
        self.assertEqual(result_expected, final_result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
