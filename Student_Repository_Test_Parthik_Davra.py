"""
this code has test cases for the compare tables of student, instructor and majors Repository
Name: Parthik Davra
CWID: 10469593
"""
# all imports
import os
import unittest
from HW10_Parthik_Davra import Repository, Student, Instructor, Major


class MajorTest(unittest.TestCase):
    """ test cases for Major calss methods in Repository """

    def test_majors_table_data(self) -> None:
        """ verify that all data in Majors table is correct """

        self.repository: Repository = Repository("D:\CS-810\Hw09")

        final_result: List[str] = [majors.majors_detail()
                                   for majors in self.repository._majors.values()]
        result_expected: List[str] = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                                       ['CS 501', 'CS 513', 'CS 545']],
                                      ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'],
                                       ['SSW 540', 'SSW 565', 'SSW 810']]]
        wrong_result: List[str] = []
        majors_table: PrettyTable = self.repository.majors_pretty_table()

        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)


class StudentTest(unittest.TestCase):
    """ test cases for Student calss methods in Repository """

    def test_student_table_data(self) -> None:
        """ verify that all data in Student table is correct """

        self.repository: Repository = Repository("D:\CS-810\Hw09"
                                                 )
        final_result: List[str] = [student_name.students_details()
                                   for student_cwid, student_name in self.repository._students.items()]
        result_expected: List[str] = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                                      ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564',
                                                                     'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
                                      ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], [
                                          'SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88],
                                      ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], [
                                          'SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58],
                                      ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555',
                                                                                    'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
                                      ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], [
                                          'SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
                                      ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], [
                                          'SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                                      ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671',
                                                                         'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
                                      ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612',
                                                                                              'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
                                      ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]
        wrong_result: List[str] = []
        student_table: PrettyTable = self.repository.student_pretty_table()

        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)


class InstuctorTest(unittest.TestCase):
    """ test cases for Instructor calss methods in Repository """

    def test_instructor_table_data(self) -> None:
        """ verify that all data in Instuctor table is correct """

        self.repository: Repository = Repository("D:\CS-810\Hw09"
                                                 )
        final_result: List[str] = [tuple(instructor_detail) for instructor_data in self.repository._instructors.values(
        ) for instructor_detail in instructor_data.instructors_details()]
        result_expected: List[str] = [('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                                      ('98765', 'Einstein, A',
                                       'SFEN', 'SSW 540', 3),
                                      ('98764', 'Feynman, R',
                                       'SFEN', 'SSW 564', 3),
                                      ('98764', 'Feynman, R',
                                       'SFEN', 'SSW 687', 3),
                                      ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                                      ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                                      ('98763', 'Newton, I',
                                       'SFEN', 'SSW 555', 1),
                                      ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                                      ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                                      ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                                      ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                                      ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)]
        wrong_result: List[str] = []
        instructor_table: PrettyTable = self.repository.instructor_pretty_table()
        self.assertEqual(result_expected, final_result)
        self.assertNotEqual(result_expected, wrong_result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
