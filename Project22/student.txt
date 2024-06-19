CREATE TABLE Students (
    STU_NUM CHAR(6) PRIMARY KEY,
    STU_SNAME VARCHAR(15) NOT NULL,
    STU_FNAME VARCHAR(15) NOT NULL,
    STU_INITIAL CHAR(1) NOT NULL,
    STU_STARTDATE DATE NOT NULL,
    COURSE_CODE CHAR(3),
    PROJ_NUM INT
);


-- Insert data into the Student table
INSERT INTO Students (STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM) VALUES
('01', 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
('02', 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
('03', 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
('04', 'Lannister', 'Cercei', 'J', '2012-09-05', '101', 2),
('05', 'Greyjoy', 'Theon', 'I', '2015-12-09', '402', 14),
('06', 'Tyrell', 'Margaery', 'Y', '2017-07-12', '305', 10),
('07', 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5);


-- Retrieve all records from Students table
SELECT '** Insert the Data **' AS output;

SELECT *
FROM Students;

-- Retrieve all records from Students table
SELECT '' AS output;
SELECT '** Students Course_code 305 **' AS output;



-- Retrieve records with Course Code of '305'

SELECT * FROM Students
WHERE COURSE_CODE = '305';

-- Update Course code to '304' for the student with STU_NUM '07'
UPDATE Students
SET COURSE_CODE = '304'
WHERE STU_NUM = '07';

-- Retrieve all records from Students table
SELECT '' AS output;
SELECT '** Update Course code **' AS output;

SELECT *
FROM Students;

-- Delete the row for the Student with Title 'Jamie Lannister'
DELETE FROM Students
WHERE STU_SNAME = 'Lannister' AND STU_FNAME = 'Jamie' AND STU_STARTDATE = '2012-09-05' 
AND COURSE_CODE = '101' AND PROJ_NUM = 2;

-- Retrieve all records from Students table
SELECT '' AS output;
SELECT '** Delete Student Jamie **' AS output;

SELECT *
FROM Students;

-- Update PROJ_NUM for all students who started before 2016 and with a corse code of atleast 201 
UPDATE Students
SET PROJ_NUM = 14
WHERE STU_STARTDATE < '2016-01-01' AND COURSE_CODE >= '201';

-- Retrieve all records from Students table
SELECT '' AS output;
SELECT '** Update Project Number**' AS output;

SELECT *
FROM Students;

-- Delete the Students table entirely
SELECT '' AS output;
SELECT '** DROP Table **' AS output;

DROP TABLE IF EXISTS Students;
