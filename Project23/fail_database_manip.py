'''Creating a SQLite database to manage the student: id, name and grade. '''
import os  # importing os
import sqlite3  # importing sqlite

# creatiog a variable to construct the path
directory = os.path.dirname(__file__)
db_directory = os.path.join(directory, "data/python_programming_db.db")
# attempt to connect to the db
try:
    db = sqlite3.connect(db_directory)
# Asks user to open a 'data' folder to place the db in
except sqlite3.OperationalError:
    print("data folder missing, Please create and run again")
    exit()
# Creating a cursor variable
cursor = db.cursor()
"""Creating a table with the id, name and grade."""
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        grade INTEGER
                )
            ''')
# create and commit python_programming table
db.commit()
python_programming_students = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99)]
"""insert data into the table with tuple"""
cursor.executemany('''
    INSERT OR REPLACE INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', python_programming_students)
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
print("\n-Initial Table With Values \n")
for row in cursor:  # print statement to iterate through each item
    print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")

cursor.execute(
    '''SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80''')
# all students with id 60<id<80
print("\n-Students with grades between 60 and 80 \n")
for row in cursor:
    print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")


cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''',
               (65, "Carl Davis"))     # update carl to 65
db.commit()

cursor.execute('''SELECT * FROM python_programming WHERE name = ?''',
               ('Carl Davis',))
# Updating and printing the data for Carl Davis
print("\n-Updated Carl Davis \n")
for row in cursor:
    print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")

cursor.execute('''DELETE FROM python_programming WHERE name = ?''',
               ("Dennis Fredrickson",))  # delete Dennis
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
print("\n-Deleted Dennis Fredrickson \n")
for row in cursor:
    print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")

cursor.execute('''UPDATE python_programming SET grade = ? WHERE id > ? ''',
               (80, 55))     # update grades for students
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
print("\n-Updated grades to 80 for all with id's larger than 55 \n")
for row in cursor:
    print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")
# close the Database
db.close()
