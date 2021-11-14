"""
One project can have multiple apps

run command
    django-admin startproject mysite .

    project name mysite
    location . means current folder

This will create a folder

    mysite
    |    |___  __init__.py
    |    |___  asgi.py          -> config file needs change when deploy on asgi server
    |    |___  settings.py      -> contains all setting like timezone, folder for static files , etc
    |    |___  urls.py          -> contains routing URLS of different functionalities
    |    |___  wsgi.py          -> config file needs change when deploy on wsgi server
    |
    |___  manage.py             -> do not normally change

Run Django project

>>    python manage.py runserver

WARNING::

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.


 >> Run 'python manage.py migrate' to apply them.

 By default uses SQLite3
 Queries that will create some default database tables  (sqlite3)

After creating tables (mostly admin related)

http://127.0.0.1:8000/admin/login/?next=/admin/

we can create an admin user and login through that


"""