-- Name: Parthik Davra
-- CWID: 10469593
-- Query5: Display each student's name,  CWID, course, grade, and the instructor's name  for all students and grades.  The result should be sorted by the student's name.

SELECT student.Name AS Student_Name, student.CWID, grade.Course, grade.Grade, instructor.Name AS Instructors_Name
FROM students AS student
JOIN grades AS grade ON grade.StudentCWID = student.CWID
JOIN instructors AS instructor ON  grade.InstructorCWID = instructor.CWID
ORDER BY student.Name;