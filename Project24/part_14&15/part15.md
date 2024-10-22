Investigate and document the procedures for performing Django database
migrations to a server-based relational database like MariaDB.

Steps

1.Install required database eg( pip install django mysqlclient)
2.Update your Django project's settings.py to configure the connection to your MariaDB
eg-DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # database engine
        'NAME': 'database_name',          # name of the database
        'USER': 'database_user',          # database user
        'PASSWORD': 'database_password',  # database password
        'HOST': 'database_host',          #  Database host, e.g., 'localhost' or an IP address
        'PORT': '3306',                   # Default port for MariaDB
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',         # Character set to handle a wide range of characters
        }
    }
}
These configurtations affect how your django project connects to the database. 
3.Create the project (django-admin startproject project_name),
cd into directory(eg-cd project_name)
 and create migrations (python manage.py makemigrations)
4.Apply migrations(python manage.py migrate)
5.View migration status(python manage.py showmigrations)
6.Any model changes and apply (makemigrations and migrate)
7.Back up(mysqldump -u database_user -p database_name > backup_file.sql)
and restore the database (mysql -u database_user -p database_name < backup_file.sql)
Following these steps ensures your database changes with the application.