SELECT FirstName, LastName, IsActive, AdvisorID, Gender 
FROM Students 
WHERE IsActive = '1' AND Gender = 'M' AND AdvisorID in (1,3);

SELECT FirstName, LastName 
FROM Students 
WHERE BIO IS NULL;

SELECT ClassID, ClassCode, ClassName, ClassDescription 
FROM Classes 
WHERE ClassID LIKE "ENG%";

SELECT Students.FirstName, Students.LastName, Students.DOB, Students.Gender, Students.GPA, Advisors.advFirstName, Advisors.advLastName
FROM Students INNER JOIN Advisors
ON Students.AdvisorID = Advisor.AdvisorID
ORDER BY Advisors.advLastName, Students.LastName ASC;

SELECT COUNT (StudentID) AS "80's"
FROM Students
WHERE DOB BETWEEN '1/1/1980' AND '12/31/1989';

SELECT AVG(GPA), Gender
FROM Students
WHERE GPA <> 0
GROUP BY Gender
ORDER BY Gender ASC;

SELECT Advisors.advFirstName, Advisors.advLastName, Count(Students.StudentID)
AS StudentCount
FROM Advisors LEFT JOIN Students
ON Advisors.AdvisorID = Students.AdvisorsID
GROUP BY Advisors.advLastName, Advisors.advFirstName;
HAVING Count(Students.StudentID) <= 1;