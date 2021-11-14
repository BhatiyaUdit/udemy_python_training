"""

>> python manage.py startapp blog

This will create a directory having the app files

blog
    |-> migrations
    |        |-> __init_.py     --> Generally used for Database migration not usually changed
    |
    |-> __init_.py              --> To run some code during start
    |-> admin.py                --> contains code for admin interface discuss later
    |-> apps.py                 --> Config file related to blog app --> usually unchanged
    |-> models.py               --> Model file as per MVC arch handle Database related stuff
    |-> tests.py                --> Used for writing tests
    |-> views.py                --> Used for writing views that will act as intermediate b/w model and html pages

Final Step register the app to Project

    mysite > setting.py > installed_apps list add 'blog'


"""