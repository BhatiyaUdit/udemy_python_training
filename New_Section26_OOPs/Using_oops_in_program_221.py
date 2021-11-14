# Example Taken from previous section of functions that do CRUD operations
import sqlite3


class Demo:
    def __init__(self):
        print("INIT CALLED with self as :: ", self)

    def create_table(self):
        connection = sqlite3.connect("my_database.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS my_table ( id INTEGER , name TEXT, salary REAL)")
        connection.commit()
        connection.close()

    def view(self):
        connection = sqlite3.connect("my_database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * from my_table")
        rows = cursor.fetchall()
        connection.close()
        return rows

    def insert(self, my_id, name, salary):
        connection = sqlite3.connect("my_database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO my_table VALUES(?, ?, ?)", (my_id, name, salary))
        connection.commit()
        connection.close()

    def __del__(self):
        print("DELETE CALLED", self)

# init is equivalent to constructor
