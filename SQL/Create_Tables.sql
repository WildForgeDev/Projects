CREATE TABLE Advisors(
    AdvisorID int IDENTITY (1,1) PRIMARY KEY NOT NULL,
    advFirstName VARCHAR(50) NOT NULL,
    advLastName VARCHAR(50) NOT NULL,
    advEmailAddress VARCHAR(50) NOT NULL
);
CREATE TABLE Students(
    StudentID int IDENTITY (1,1) PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    StartDate Date NOT NULL,
    BIO VARCHAR(1500) NULL,
    GPA DECIMAL(3,2) NULL,
    IsActive BIT NOT NULL,
    AdvisorID INT NOT NULL,
    Gender CHAR(1) NOT NULL,
);

DROP TABLE Advisors;

CREATE TABLE Students_Classes(
    StudentClassId INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    StudentId INT NOT NULL,
    ClassId INT NOT NULL,
    Assignment1 DECIMAL(3,0) NULL,
    Assignment2 DECIMAL(3,0) NULL,
    Assignment3 DECIMAL(3,0) NULL,
    Assignment4 DECIMAL(3,0) NULL,
    GPA DECIMAL(3,2) NULL,
);

Create TABLE Classes(
    ClassId INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    ClassCode VARCHAR(10) NOT NULL,
    ClassName VARCHAR(70) NOT NULL,
    ClassDescription VARCHAR(1500) NOT NULL
);

ALTER TABLE Students
ADD FOREIGN KEY(AdvisorID)
REFERENCES
Advisors(AdvisorID);

ALTER TABLE Students_Classes
ADD FOREIGN KEY(StudentId)
REFERENCES
Students(StudentId);

ALTER TABLE Student_Classes
ADD FOREIGN KEY(ClassId)
REFERENCES
Classes(ClassId);