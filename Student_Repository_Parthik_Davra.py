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
        self._majors: Dict[str, Major] = dict()

        try:
            student_path: str = os.path.join(path, 'students.txt')
            instructor_path: str = os.path.join(path, 'instructors.txt')
            grades_path: str = os.path.join(path, 'grades.txt')
            majors_path: str = os.path.join(path, 'majors.txt')
            self._read_majors_data(majors_path)
            self._read_student_data(student_path)
            self._read_instructor_data(instructor_path)
            self._read_grades_data(grades_path)
            self.majors_pretty_table()
            self.student_pretty_table()
            self.instructor_pretty_table()

        except (FileNotFoundError, ValueError) as e:
            print("file can not found at defiend path or value is not correct.")

    def _read_student_data(self, path: str) -> None:
        """ read students data using file reader function and add data to dictionary """

        try:
            for student_cwid, student_name, student_major in file_reader(path, 3, sep=';', header=True):

                if student_major in self._majors:
                    self._students[student_cwid] = Student(
                        student_cwid, student_name, self._majors[student_major])
                else:
                    print(
                        f"Can not find major {student_major} of student {student_name}")
        except ValueError as error:
            print(f"There is error with Student data: {error}")

    def _read_instructor_data(self, path: str) -> None:
        """ read instructor data using file reader function and add data to dictionary """

        try:
            for instructor_cwid, instructor_name, instructor_dept in file_reader(path, 3, sep='|', header=True):
                self._instructors[instructor_cwid] = Instructor(
                    instructor_cwid, instructor_name, instructor_dept)
        except ValueError as error:
            print(f"There is error with Instructor data: {error}")

    def _read_grades_data(self, path: str) -> None:
        """ read grades data for student and instructor using file reader function and add data to dictionary """

        try:
            for student_cwid, student_course, student_grade, instructor_cwid in file_reader(path, 4, sep='|', header=True):
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

    def _read_majors_data(self, path: str):
        """ read majiors data for the student and instructor using file reader function and add data to dictionary """

        try:
            for student_major, course_type, student_course in file_reader(path, 3, sep='\t', header=True):
                if student_major not in self._majors:
                    self._majors[student_major] = Major(student_major)
                self._majors[student_major].add_all_courses(
                    student_course, course_type)
        except ValueError as error:
            print(f"There is error with Majors data: {error}")

    def student_pretty_table(self) -> None:
        """ Student pretty table for print table"""
        table: PrettyTable = PrettyTable()
        table.field_names = Student.field_header
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

    def majors_pretty_table(self) -> None:
        """ Majors table for print table """
        table: PrettyTable = PrettyTable(field_names=Major.field_header)
        for major in self._majors.values():
            table.add_row(major.majors_detail())
        print("\nMajors Table")
        print(table)
        return table


class Major:
    """ Major Class for Repository """
    field_header: List[str] = [
        'Major', 'Required Courses', 'Electives Courses']

    def __init__(self, major: str) -> None:
        """ Intialization of major class field """
        self._major: str = major
        self._required: Set[str] = set()
        self._electives: Set[str] = set()

    def add_all_courses(self, course: str, type: str) -> None:
        """" add courses either elective or required in dictionary """
        try:
            if type == 'E':
                self._electives.add(course)
            elif type == 'R':
                self._required.add(course)
            else:
                raise ValueError("Valid courses are not given")
        except ValueError as error:
            print(error)

    def remaining_courses(self, completed_courses: Dict[str, str]) -> Tuple[str, List[str], List[str], List[str]]:
        """ Add remaining courses and electives courses """
        try:
            grades: Set[str] = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

            pass_student_courses: Set[str] = {course for course,
                                              grade in completed_courses.items() if grade in grades}
            remaining_courses: Set[str] = self._required - pass_student_courses
            electives_courses: Set[str] = self._electives

            if self._electives.intersection(pass_student_courses):
                electives_courses = []

            return self._major, list(pass_student_courses), list(remaining_courses), list(electives_courses)
        except ValueError as error:
            print(error)

    def majors_detail(self) -> Tuple[str, List[str], List[str]]:
        """ Returns majors information data """
        return [self._major, sorted(self._required), sorted(self._electives)]


class Student:
    """Student Class for Repository """
    field_header: List[str] = ['CWID', 'Name', 'Major',
                               'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA']

    def __init__(self, student_cwid: str, student_name: str, student_major: str) -> None:
        """ Intialization of student class field """
        self._cwid: str = student_cwid
        self._name: str = student_name
        self._major: str = student_major
        self._courses: Dict[str, str] = dict()

    def add_course(self, student_course: str, student_grade: str) -> None:
        """ Add courses data with grade """
        self._courses[student_course] = student_grade

    def gpa(self) -> float:
        """Calculate the GPA and add to the dictionary"""

        grades_range: Dict[str, float] = {'A': 4.0, 'A-': 3.75, 'B+': 3.25, 'B': 3.0, 'B-': 2.75,
                                          'C+': 2.25, 'C': 2.0, "C-": 0.00, "D+": 0.00, "D": 0.00, "D-": 0.00, "F": 0.00}
        try:
            gpa_total: float = sum(
                [grades_range[grade] for grade in self._courses.values()]) / len(self._courses.values())
            return round(gpa_total, 2)
        except ZeroDivisionError as error:
            print(f"Zero division error: {error}")

    def students_details(self) -> Tuple[str, str, str, List[str], List[str], List[str]]:
        """ Returns student information """

        student_major, passed_student, remaining_courses, electives_courses = self._major.remaining_courses(
            self._courses)

        return [self._cwid, self._name, student_major, sorted(passed_student), sorted(remaining_courses), sorted(electives_courses), self.gpa()]


class Instructor:
    """ Instructor class for Repository """
    field_header: List[str] = ['CWID', 'Name', 'Dept', 'Course', 'Students']

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
