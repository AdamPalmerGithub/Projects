list_marks_by_julia_sql = """
SELECT Student.mark
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.teacher_name = 'Julia Python';
"""

cur.execute(list_marks_by_julia_sql)