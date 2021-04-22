"""
this code calculate the GPA for the student and track of all the courses for student, instructor and major class Repository
Name: Parthik Davra
CWID: 10469593
"""

# all imports
import os
from collections import defaultdict
from prettytable import PrettyTable
from typing import Dict, DefaultDict, Tuple, List, Iterator, Set
from HW08_Parthik_Davra import file_reader


class Repository:
    """ Repository class which has Student, Instructor and Majors classes """

    def __init__(self, path: str, tables: bool = True) -> None:
        """ initialization of repository data """
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()

        try:
            student_path: str = os.path.join(path, 'students.txt')
            instructor_path: str = os.path.join(path, 'instructors.txt')
            grades_path: str = os.path.join(path, 'grades.txt')
            self._read_student_data(student_path)
            self._read_instructor_data(instructor_path)
            self._read_grades_data(grades_path)
            self.student_pretty_table()
            self.instructor_pretty_table()

        except (FileNotFoundError, ValueError) as e:
            print("file can not found at defiend path or value is not correct.")

    def _read_student_data(self, path: str) -> None:
        """ read students data using file reader function and add data to dictionary """

        try:
            for student_cwid, student_name, student_major in file_reader(path, 3, sep='\t', header=False):

                if student_cwid in self._students:
                    raise KeyError(
                        f"Student with {student_cwid} already exist in student data.")
                else:
                    self._students[student_cwid] = Student(
                        student_cwid, student_name, student_major)
        except ValueError as error:
            print(f"There is error with Student data: {error}")

    def _read_instructor_data(self, path: str) -> None:
        """ read instructor data using file reader function and add data to dictionary """

        try:
            for instructor_cwid, instructor_name, instructor_dept in file_reader(path, 3, sep='\t', header=False):
                if instructor_cwid in self._instructors:
                    raise KeyError(
                        "Instructor with CWID is already in the file")
                self._instructors[instructor_cwid] = Instructor(
                    instructor_cwid, instructor_name, instructor_dept)
        except ValueError as error:
            print(f"There is error with Instructor data: {error}")

    def _read_grades_data(self, path: str) -> None:
        """ read grades data for student and instructor using file reader function and add data to dictionary """

        try:
            for student_cwid, student_course, student_grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):
                if student_cwid not in self._students:
                    print(f'{student_cwid} are the students grade')
                else:
                    self._students[student_cwid].add_course(
                        student_course, student_grade)

                if instructor_cwid not in self._instructors:
                    print(f'{student_cwid} are the instructor grade')
                else:
                    self._instructors[instructor_cwid].add_student(
                        student_course)
        except ValueError as error:
            print(f"There is error with Grades data: {error}")

    def student_pretty_table(self) -> None:
        """ Student pretty table for print table"""
        table: PrettyTable = PrettyTable(field_names=Student.field_header)
        for student in self._students.values():
            table.add_row(student.students_details())
        print("\nStudent Table ")
        print(table)
        return table

    def instructor_pretty_table(self) -> None:
        """ Instructor table for print table """
        table: PrettyTable = PrettyTable(field_names=Instructor.field_header)
        for instructor in self._instructors.values():
            for row in instructor.instructors_details():
                table.add_row(row)
        print("\nInstructor Table ")
        print(table)
        return table

class Student:
    """Student Class for Repository """
    field_header: List[str] = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, student_cwid: str, student_name: str, student_major: str) -> None:
        """ Intialization of student class field """
        self._cwid: str = student_cwid
        self._name: str = student_name
        self._major: str = student_major
        self._courses: Dict[str, str] = dict()

    def add_course(self, student_course: str, student_grade: str) -> None:
        """ Add courses data with grade """
        self._courses[student_course] = student_grade

    def students_details(self) -> Tuple[str, str, str, List[str], List[str], List[str]]:
        """ Returns student information """
        return [self._cwid, self._name, sorted(self._courses.keys())]
 

class Instructor:
    """ Instructor class for Repository """
    field_header: List[str] = [
        "CWID", "Name", "Dept", "Course", "Students"]


    def __init__(self, instructor_cwid: str, instructor_name: str, instructor_dept: str) -> None:
        """ Intialization of instructor class field """
        self._cwid: str = instructor_cwid
        self._name: str = instructor_name
        self._dept: str = instructor_dept
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def add_student(self, student_course: str) -> None:
        """ student takes the course with professor """
        self._courses[student_course] = self._courses[student_course] + 1

    def instructors_details(self) -> Iterator[Tuple[str, str, str, str, int]]:
        """ Returns instructor information """

        for instructors_course, instructors_count in self._courses.items():
            yield [self._cwid, self._name, self._dept, instructors_course, instructors_count]


def main():
    # Repository location
    Repository('HW10_Test')


if __name__ == '__main__':
    main()
