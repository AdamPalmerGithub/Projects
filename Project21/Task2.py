# === Create SQLite Database and tables with Sqlite script

import sqlite3
# ====== Create the School.db
conn = sqlite3.connect("School.db")

# Create a curser object
cur = conn.cursor()


#SQL script to create course table
create_course_table_sql = """ 
DROP TABLE IF EXISTS Course;

CREATE TABLE Course (
    course_code CHAR(5) PRIMARY KEY,
    course_name VARCHAR(30) NOT NULL,
    course_description TEXT NOT NULL,
    teacher_name VARCHAR(30) NOT NULL,
    course_level INTEGER CHECK(course_level in (1, 2, 3)) NOT NULL
);
"""
# Execute the SQL script
cur.executescript(create_course_table_sql)
conn.commit()

#scrip to create student object
create_student_table_sql = """
DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
    student_id CHAR(13) PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    stu_subject_code CHAR(5) NOT NULL,
    mark INTEGER NOT NULL,
    FOREIGN KEY(stu_subject_code) REFERENCES Course(course_code)
);

"""
# Execute the SQL script
cur.executescript(create_student_table_sql)
conn.commit()

#insert data into course table
insert_courses_sql = """
INSERT INTO Course 
VALUES
('DS01', 'Python for Data Science', 'This course provides an introductory basis to learning Python.', 'Monty Python', 1),
('DS02', 'Data Analytics and Exploration', 'Techniques for exploring and manipulating data are covered here. This covers reading, converting, visualising, analysing and preprocessing data.', 'Frank Google', 2),
('DS03', 'Machine Learning', 'Introduces students to important machine learning concepts, enabling them to handle big data in a useful manner.', 'Andrew Ng', 3),
('WD01', 'Web Dev Fundamentals', 'Provides a basis to Javascript and all fundamental tools.', 'Mark Zuckerberg', 1),
('WD02', 'Web Dev Frameworks', 'This course aims to provie an understanding of all important frameworks in developing web apps.', 'Zucc Markerberg', 2),
('WD03', 'Client-Server Programming', 'This course challenges students to use what they have learned to build complex web apps.', 'William Gates', 3),
('DB01', 'Files', 'Provides a basis of file inputs and outputs as well as data storage.', 'Sata Drivehard', 1),
('DB02', 'SQL', 'This is the sequel to DB01 - Files.', 'Sata Drivehard', 2),
('DB03', 'Database Management', 'A course on how to be a database admin.', 'Sata Drivehard', 3),
('SE01', 'Introduction to Programming', 'Provides the students with a simple programming language to get the basics.', 'Julia Python', 1),
('SE02', 'Advanced Programming', 'Touches on more advanced algorithms and data structures.', 'Ruby Java', 2),
('SE03', 'Software Engineering', 'An exploration of various development patterns and best practices.', 'Julia Python', 3)
;
"""
cur.executescript(insert_courses_sql)
conn.commit()

#insert data into student table
insert_students_sql = """
INSERT INTO Student 
VALUES
('JV00100200304', 'Johnny', 'Valker', 'jv@email.com', 'DS02', 64),
('JS00100200305', 'Jack', 'Sparrow', 'js@blackpearl.com', 'WD01', 52),
('LM00100200306', 'Luffy', 'Monkey', 'pking@linegrand.com', 'WD03', 43),
('PA00100200307', 'Paul', 'Atreides', 'paul@melange.com', 'DS01', 78),
('LA00100200308', 'Leto', 'Atreides', 'leto@melange.com', 'DS03', 92),
('AT00100200309', 'Alan', 'Turing', 'whereis@myemail.com', 'SE01', 72),
('AL00100200310', 'Ada', 'Lovelace', 'motherof@computing.com', 'SE03', 86),
('PP00100200311', 'Peter', 'Parker', 'pp@marvel.com', 'WD03', 83),
('AS00100200312', 'Anthony', 'Stark', 'ironman@marvel.com', 'SE02', 95),
('KK00100200313', 'Kamala', 'Khan', 'ms@marvel.com', 'DS01', 67),
('CD00100200314', 'Carol', 'Danvers', 'captain@marvel.com', 'WD02', 72),
('DV00100200315', 'Darth', 'Vader', 'dv@deathstar.com', 'SE03', 62),
('AS00100200316', 'Anakin', 'Skywalker', 'ihatesand@deathstar.com', 'SE02', 62),
('LS00100200317', 'Leia', 'Skywalker', 'leader@rebels.com', 'DS03', 89),
('OK00100200318', 'Obi-Wan', 'Kenobi', 'hellothere@jedicouncil.com', 'DS01', 70),
('GG00100200319', 'Gandalf', 'Grey', 'youshall@notpass.com', 'WD02', 27),
('JB00100200320', 'Johnny', 'Bravo', 'jb@cn.com', 'DB02', 69),
('PB00100200321', 'Pinky', 'Brain', 'pinky@brain.com', 'DS01', 100),
('JS00100200322', 'John', 'Smith', 'doctor@who.com', 'DB03', 79),
('JS00100200323', 'Jane', 'Smith', 'professor@who.com', 'DB03', 92),
('EP00100200324', 'Elvis', 'Presley', 'elvis@elvis.com', 'SE01', 56),
('FM00100200325', 'Frederick', 'Mercury', 'rhapsody@queen.com', 'WD03', 87),
('BC00100200326', 'Benedict', 'Cumberbatch', 'benny@strange.com', 'DB01', 65),
('WT00100200327', 'Wimbledon', 'Tennismatch', 'wimbeldon@strange.com', 'DB02', 68)
;
"""
cur.executescript(insert_students_sql)
conn.commit()

#SQL query to list names and surnames of all students doing the DS03 course
list_students_in_ds03_sql = """
SELECT Student.email 
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.course_level = 3;
"""

#Execute the query
cur.execute(list_students_in_ds03_sql)

# SQL query to list email addresses of all students doing a level 3 course
list_emails_level_3_sql = """
SELECT Student.email 
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.course_level = 3;
"""

# Execute the query
cur.execute(list_emails_level_3_sql)

#SQL query to sort the names of students with 70 or higher  with the course name
list_students_above_70_sql = """
SELECT Student.first_name, Course.course_name
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Student.mark >= 70;
"""
#Execute the query
cur.execute(list_students_above_70_sql)

# SQL query to sort marks of students taught by Julia Python
list_marks_by_julia_sql = """
SELECT Student.mark
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.teacher_name = 'Julia Python';
"""

# Execute the query
cur.execute(list_marks_by_julia_sql)


conn.close()










# machine_learning_sql = """
# CREATE TABLE Student (
#     student_id CHAR(13) PRIMARY KEY,
#     first_name VARCHAR(30) NOT NULL,
#     last_name VARCHAR(30) NOT NULL,
#     email VARCHAR(30) NOT NULL,
#     stu_subject_code CHAR(5) NOT NULL,
#     mark INTEGER NOT NULL,
#     FOREIGN KEY(stu_subject_code) REFERENCES Course(course_code)
# );

# """
# # Execute the SQL script
# cur.execute(machine_learning_sql)
# conn.commit()
