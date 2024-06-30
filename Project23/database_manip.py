'''Creating a SQLite database to manage the student: id, name and grade. '''
import os  # importing os
import sqlite3  # importing sqlite
import sys  # import sys for exit

# creating a variable to construct a path
directory = os.path.dirname(__file__)
db_directory = os.path.join(directory, "data/python_programming_db.db")

# attempt to connect to the database
# Set up db and cursor variable
try:
    db = sqlite3.connect(db_directory)
    cursor = db.cursor()

    # open the table with id, name and grade
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            grade INTEGER
    )''')
        db.commit()
    except sqlite3.OperationalError:
        print("Error creationg table")

        # attempts to add data to the table
    try:
        python_programming_students = [
            (55, "Carl Davis", 61),
            (66, "Dennis Fredrickson", 88),
            (77, "Jane Richards", 78),
            (12, "Peyton Sawyer", 45),
            (2, "Lucas Brooke", 99)]
        cursor.executemany('''
            INSERT OR REPLACE INTO python_programming(id, name, grade)
            VALUES(?,?,?)''', python_programming_students)
        db.commit()

        # message to confirm data has been added
        cursor.execute('''SELECT * FROM python_programming''')
        print("\n-Initial Table With Values \n")
        for row in cursor:
            print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")

    # if adding fails, return error message and rollback
    except sqlite3.OperationalError:
        print("Error adding data to table")
        if db:
            db.rollback()

    # prints all students with grade 60-80
    try:
        cursor.execute('''
                       SELECT * FROM python_programming
                       WHERE grade BETWEEN 60 AND 80''')

        print("\n-Students with grades between 60 and 80 \n")
        for row in cursor:
            print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")
    # Error message
    except sqlite3.OperationalError:
        print("Error retrieving data for range 60-80")

    # updates carl davis grade
    try:
        cursor.execute('''
                       UPDATE python_programming
                       SET grade = ?
                       WHERE name = ?
                    ''', (65, "Carl Davis"))     # update carl to 65
        db.commit()

        # print the update
        cursor.execute('''SELECT * FROM python_programming WHERE name = ?''',
                       ('Carl Davis',))
        print("\n-Updated Carl Davis \n")
        for row in cursor:
            print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")
    # roll back if error
    except sqlite3.OperationalError:
        print("Error updating Carl Davis")
        if db:
            db.rollback()

    # delete dennis
    try:
        cursor.execute('''DELETE FROM python_programming WHERE name = ?''',
                       ("Dennis Fredrickson",))
        db.commit()

        # print updated table
        cursor.execute('''SELECT * FROM python_programming''')
        print("\n-Deleted Dennis Fredrickson \n")
        for row in cursor:
            print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")
    # print and rollback errors
    except sqlite3.OperationalError:
        print("Error deleting Dennis")
        if db:
            db.rollback()

    # update students with id > 55
    try:
        cursor.execute(
            '''UPDATE python_programming SET grade = ? WHERE id > ? ''',
            (80, 55))
        db.commit()

        # print updated list
        cursor.execute('''SELECT * FROM python_programming''')
        print("\n-Updated grades to 80 for all with id's larger than 55 \n")
        for row in cursor:
            print(f"Student ID: {row[0]} Name: {row[1]} Grade: {row[2]}")
    # print and rollback errors
    except sqlite3.OperationalError:
        print("Error updating grades when id>55")

# error connecting to database
except sqlite3.OperationalError:
    print("data folder missing, Please create and run again")
    sys.exit()

# close the database
finally:
    db.close()
