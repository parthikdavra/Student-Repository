-- Name: Parthik Davra
-- CWID: 10469593
-- Query2: What is the total number of students by major?

SELECT Major, COUNT(*) AS 'Total_Number_Of_Students' FROM students GROUP BY Major;