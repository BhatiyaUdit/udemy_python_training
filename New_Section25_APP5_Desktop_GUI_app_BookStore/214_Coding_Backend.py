import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books 
            (   id INTEGER PRIMARY KEY, 
                title VARCHAR, 
                author text,
                year INTEGER, 
                ISBN INTEGER
            )
    """)
    connection.commit()
    connection.close()


def insert_book(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    connection.set_trace_callback(print)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books VALUES ( NULL , ? ,? ,? ,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view_all():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(**kwargs):
    title_clause, author_clause, year_clause, isbn_clause = "", "", "", ""
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE 1=1"
    if kwargs.get('title'):
        title_clause = f" AND title = '{kwargs.get('title')}'"

    if kwargs.get('author'):
        author_clause = f" AND author = '{kwargs.get('author')}'"

    if kwargs.get('year'):
        year_clause = f" AND year = '{kwargs.get('year')}'"

    if kwargs.get('isbn'):
        isbn_clause = f" AND isbn = '{kwargs.get('isbn')}'"

    sql = sql + title_clause + author_clause + year_clause + isbn_clause
    print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("books.db")
    connection.set_trace_callback(print)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books where id = ?", (id,))
    connection.commit()
    connection.close()


def update(id, **kwargs):
    title_clause, author_clause, year_clause, isbn_clause = "", "", "", ""
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = f"UPDATE books SET id = '{id}'"
    if kwargs.get('title'):
        title_clause = f" , title = '{kwargs.get('title')}'"

    if kwargs.get('author'):
        author_clause = f" , author = '{kwargs.get('author')}'"

    if kwargs.get('year'):
        year_clause = f" , year = '{kwargs.get('year')}'"

    if kwargs.get('isbn'):
        isbn_clause = f" , isbn = '{kwargs.get('isbn')}'"

    where_clause = f" WHERE id = '{id}'"
    sql = sql + title_clause + author_clause + year_clause + isbn_clause + where_clause
    print(sql)
    cursor.execute(sql)
    connection.close()


#
# connect()
# insert_book("Udit", "Udit", 1996, 123456)
# print(view_all())
# INTEGER Primary key is auto incremented but numeric does not

# print(search(author='', year=0))
# delete(6)
# print(view_all())
# update(5, author='New Auth', title="New Tie", year=1555)
