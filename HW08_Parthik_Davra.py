"""
In this code we practice on function like datetime,files & prettytable
Author: Parthik davra
CWID: 10469593
"""

# all imports
from datetime import datetime, timedelta
from typing import Tuple, List, Dict, IO, Iterator
import os
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ this function return tuple with three days after the given date and count total days between date """

    THREE_DAYS_AFTER: int = 3
    three_days_after_02272020: datetime = datetime(
        2020, 2, 27) + timedelta(days=THREE_DAYS_AFTER)
    three_days_after_02272019: datetime = datetime(
        2019, 2, 27) + timedelta(days=THREE_DAYS_AFTER)
    days_passed_02012019_09302019: int = (
        datetime(2019, 9, 30) - datetime(2019, 2, 1))

    return (three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019).days


def file_reader(path: str, fields: str, sep: str = ',', header: bool = False) -> Iterator[List[str]]:
    """ this function return file name, numberr of line, number of field and line number where problem occured """

    # check if the file is valid at given path
    try:
        current_file: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Please enter valid path for file, Not found file at location {path}")
    else:

        with current_file:
            for line_number, line in enumerate(current_file, 1):
                single_row: List[str] = line.rstrip("\n").split(sep)

                # check if line has same field as expected
                if len(single_row) != fields:
                    current_file.close()
                    raise ValueError(
                        f"‘{path}’ has {len(single_row)} fields on line {line_number} but expected {fields}")

                if not header or line_number != 1:
                    yield tuple(single_row)


class FileAnalyzer:
    """ this class has three fucntion which return total classes, fucntions, lines and characters from python file """

    def __init__(self, directory: str) -> None:
        """ this function initialize the directory, file summary and analyze file method """

        if not os.path.exists(directory):
            raise FileNotFoundError(
                f"The specified directory ‘{directory}’ is not found")

        self.directory: str = directory
        self.file_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ this function return the total number of character, total class and function and total lines in the python file """

        path: str = self.directory
        directory: List[str] = os.listdir(path)

        for files in directory:
            if files.endswith('.py'):

                # check if directory has valid path
                try:
                    current_file = open(os.path.join(path, files), 'r')
                except FileNotFoundError:
                    raise FileNotFoundError(
                        f"please enter vlaid path, {files} is not openiong")
                else:

                    with current_file:
                        # initialize the value
                        number_of_character: int = 0
                        total_count_of_class: int = 0
                        total_count_of_function: int = 0
                        total_line_count: int = 0

                        for line in current_file:
                            number_of_character += len(line)
                            total_line_count += 1

                            # count of total def and class
                            if line.strip().startswith('def '):
                                total_count_of_function += 1
                            if line.strip().startswith('class '):
                                total_count_of_class += 1

                        self.file_summary[current_file] = {
                            'classes': total_count_of_class,
                            'functions': total_count_of_function,
                            'lines': total_line_count,
                            'Character': number_of_character
                        }

    def pretty_print(self) -> None:
        """ this function print the file_summary in table formate using pretty table """

        result: PrettyTable = PrettyTable()
        result.field_names = ['File Name', 'Classes',
                              'Fucntions', 'Lines', 'Character']

        for key, value in self.file_summary.items():
            result.add_row([key] + list(value.values()))

        print("\nSummary for ", self.directory)
        print(result)
