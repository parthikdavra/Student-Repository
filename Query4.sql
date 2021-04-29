-- Name: Parthik Davra
-- CWID: 10469593
-- Query4: Display the name and cwid of each student along with the total number of courses taken by the student.

SELECT student.CWID, student.Name, COUNT(grade.Course) AS Total_Number_Of_Course
FROM students As student
JOIN grades AS grade
WHERE student.CWID = grade.StudentCWID
GROUP BY student.CWID;