"""
This code has students result table using Flask and jinja2 
author: Parthik Davra
CWID : 10469593
"""

from typing import Dict
from flask import Flask, render_template, redirect, url_for
import sqlite3

app: Flask = Flask(__name__)
database_path: str = "D:\CS-810\HW12\Homework12\Homework11.db"


@app.route('/')
def landing() -> None:
    return render_template('landing.html', title="Welcome Page")


@app.route('/Student_grades')
def Student_grades() -> str:
    query: str = "SELECT stud.Name AS 'Student', stud.CWID, grade.Course, grade.Grade, inst.Name AS 'Instructor' " \
                 "FROM students stud JOIN grades grade ON stud.CWID=grade.StudentCWID " \
                 "JOIN instructors inst ON grade.InstructorCWID=inst.CWID ORDER BY stud.Name"
    database_connection: sqlite3.Connection = sqlite3.connect(database_path)
    headers_data: List[str] = database_connection.execute(query).description
    table: List[Dict[str, str]] = [{'student': student, 'cwid': cwid, 'course': course,
                                    'grade': grade, 'instructor': inst}
                                   for student, cwid, course, grade, inst in database_connection.execute(query)]
    database_connection.close()

    return render_template('stevens.html', title="Stevens Repository", headers=headers_data, table=table)


app.run(debug=True)
