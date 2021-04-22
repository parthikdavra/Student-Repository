"""
In this code, we are writing test cases for HW09
Name: Parthik Davra
CWID: 10469593  
"""

# all imports
import unittest
from Student_Repository_Parthik_Name import Repository


class StudentTest(unittest.TestCase):
    """ test cases for Student calss methods in Repository """

    def test_student_table_data(self) -> None:
        """ verify that all data in Student table is correct """
        
        self.repository: Repository = Repository(
            "D:\CS-810\HW10")
        final_result: List[str] = {cwid: student.students_details()
                  for cwid, student in self.repository._students.items()}
        result_expected: List[str] = {'10103': ['10103', 'Baldwin, C',
                              ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10115': ['10115', 'Wyatt, X',
                              ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    '10175': ['10175', 'Erickson, D',
                              ['SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183', 'Chapman, O', ['SSW 689']],
                    '11399': ['11399', 'Cordova, I', ['SSW 540']],
                    '11461': ['11461', 'Wright, U',
                              ['SYS 611', 'SYS 750', 'SYS 800']],
                    '11658': ['11658', 'Kelly, P', ['SSW 540']],
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    '11788': ['11788', 'Fuller, E', ['SSW 540']]}

        
        self.assertEqual(result_expected, final_result)

class InstructorTest(unittest.TestCase):
    """ test cases for Instructor calss methods in Repository """

    def test_instructor_table_data(self) -> None:
        """ verify that all data in Instructor table is correct """
        self.repository: Repository = Repository(
            "D:\CS-810\HW10")
        final_result: List[str] = {tuple(
            detail) for instructor in self.repository._instructors.values(
        ) for detail in instructor.instructors_details()}
        result_expected: List[str] = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                    ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        
        self.assertEqual(result_expected, final_result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
