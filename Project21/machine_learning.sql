list_students_in_ds03_sql = """
SELECT Student.email 
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.course_level = 3;
"""

cur.execute(list_students_in_ds03_sql)