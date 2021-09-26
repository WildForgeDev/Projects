CREATE TABLE Degrees_Classes(
DegreeClassId INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
DegreeClassId INT NOT NULL,
ClassId INT NOT NULL
);

CREATE TABLE Degrees(
DegreeId INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
DegreeName VARCHAR(100) NOT NULL,
Description(1000) NOT NULL
);

Alter table Students
Add Foreign Key(DegreeId)
References
Degrees(DegreeId);

ALTER TABLE Degrees_Classes
ADD FOREIGN KEY (ClassID)
REFERENCES Classes(ClassId);

ALTER TABLE Degrees_Classes
ADD FOREIGN KEY(DegreeID)
REFERENCES
Degrees(DegreeId);

INSERT INTO Degrees (DegreeName,Description)
VALUES
('BCS','Bachelor of Computer Science')
('BBA', 'Bachelor of Business Administration')
('BSW', 'Bachelor of Social Work')

UPDATE Students
SET DegreeId = 2
WHERE StudentID = 2

INSERT INTO Advisors (advFirstName,advLastName,advEmailAddress)
VALUES
('Lauren','Carey','Lauren@college.edu'),
('Stephen','Peppers','Stephen@college.edu'),
('James','Burch','James@college.edu');

INSERT INTO Students (FirstName,LastName,DOB,StartDate,BIO,GPA,IsActive,AdvisorID,Gender,DegreeId)
VALUES
('John','Lakey','4/6/1994','1/1/2016',NULL,2.7,1,1003,'M',1),
('Addison','Liberty','11/28/2000','1/1/2019',NULL,3.2,1,1004,'F',2),
('Elliana','Burch','6/29/2001','1/1/2018',NULL,3.8,1,1002,'F',3);

INSERT INTO Classes (ClassCode,ClassName,ClassDescription)
VALUES
('CS219','Python Programing','Continue Learning Python'),
('MATH111','College Algebra for Technical Programs','Learn College Algebra'),
('PHIL101','Introduction to Ethics','Learn Ethics');

INSERT INTO Students_Classes (StudentId,ClassId,Assignment1,Assignment2,Assignment3,Assignment4,GPA)
VALUES
(1002,1002,90,85,73,90,3.0),
(1003,1003,90,95,97,80,3.7),
(1004,1004,99,91,97,98,4.0);