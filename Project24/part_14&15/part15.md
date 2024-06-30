Investigate and document the procedures for performing Django database
migrations to a server-based relational database like MariaDB.

Steps

1.install required database eg pip install django mysqlclient
2.change django projects settings.py with the correct database info
3.create the project, cd into directory and create migrations
4.apply migrations
5.view migration status
6.model changes followed by makemigrations and migrate
7.Back up and restore the database
Following these steps ensures your database changes with the application.