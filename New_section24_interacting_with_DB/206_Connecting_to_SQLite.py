import sqlite3


# connection = sqlite3.connect("my_database.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS my_table ( id INTEGER , name TEXT, salary REAL)")
# cursor.execute("INSERT INTO my_table VALUES(1, 'udit', 500000.00)")
# connection.commit()
# connection.close()

#### Creating methods for above

def create_table():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table ( id INTEGER , name TEXT, salary REAL)")
    connection.commit()
    connection.close()


def insert(my_id, name, salary):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO my_table VALUES(?, ?, ?)", (my_id, name, salary))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from my_table")
    rows = cursor.fetchall()
    connection.close()
    return rows


# insert(2, 'abcd', 1000)
print(view())
