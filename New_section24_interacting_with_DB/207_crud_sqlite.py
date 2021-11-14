import sqlite3


def insert(my_id, name, salary):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO my_table VALUES(?, ?, ?)", (my_id, name, salary))
    connection.commit()
    connection.close()


def select():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from my_table")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(my_id):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM my_table WHERE id = ?", (my_id))
    connection.commit()
    connection.close()


def update(my_id, salary):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE my_table SET salary = ? WHERE id = ?", (salary, my_id))
    connection.commit()
    connection.close()


#
# delete('2')
update('1', 800000)
print(select())
