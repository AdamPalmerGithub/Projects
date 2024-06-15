# === Create SQLite Database and tables with Sqlite script

import sqlite3
# ====== Create the School.db
conn = sqlite3.connect("School.db")

# Create a curser object
cur = conn.cursor()
#conn.close()

#SQL script to create course table
create_course_table_sql = """ 
CREATE TABLE Course (
    course_code CHAR(5) PRIMARY KEY,
    course_name VARCHAR(30) NOT NULL,
    course_description text NOT NULL,
    teacher_name varchar(30) NOT NULL,
    course_level INTEGER CHECK(course_level in (1, 2, 3)) NOT NULL
);
"""
# Execute the SQL script
cur.execute(create_course_table_sql)

