-- Name: Parthik Davra
-- CWID: 10469593
-- Query3: What is the most frequent grade for SSW 810 across all students?

SELECT Course, Grade, COUNT(Grade) AS Grade_Frequency
FROM grades
WHERE Course = 'SSW 810'
GROUP BY Grade
LIMIT 1;