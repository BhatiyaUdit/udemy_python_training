# Example Taken from previous section of functions that do CRUD operations
import sqlite3


class Demo:
    def __init__(self):
        print("INIT CALLED with self as :: ", self)
        self.connection = sqlite3.connect("my_database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS my_table ( id INTEGER , name TEXT, salary REAL)")
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * from my_table")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, my_id, name, salary):
        self.cursor.execute("INSERT INTO my_table VALUES(?, ?, ?)", (my_id, name, salary))
        self.connection.commit()

    def __del__(self):
        print("DEL CALLED with self as :: ", self)
        self.connection.close()

# init is equivalent to constructor

# del is equivalent to destructor
