import psycopg2


# must have a data base already present in postgre server
# pass database name , user name , password , host and port to the connect method


def create_table():
    connection = psycopg2.connect(dbname='database1', user='udit', password='udit1234', host='localhost')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table ( id INTEGER , name TEXT, salary REAL)")
    connection.commit()
    connection.close()


def insert(my_id, name, salary):
    connection = psycopg2.connect(dbname='database1', user='udit', password='udit1234', host='localhost')
    cursor = connection.cursor()
    # PRONE TO SQL INJECTION : #
    # cursor.execute("INSERT INTO my_table VALUES('%s', '%s', '%s')" % (my_id, name, salary))
    cursor.execute("INSERT INTO my_table VALUES(%s, %s, %s)", (my_id, name, salary))
    connection.commit()
    connection.close()


def select():
    connection = psycopg2.connect(dbname='database1', user='udit', password='udit1234', host='localhost')
    cursor = connection.cursor()
    cursor.execute("SELECT * from my_table")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(my_id):
    connection = psycopg2.connect(dbname='database1', user='udit', password='udit1234', host='localhost')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM my_table WHERE id = %s", (my_id))
    connection.commit()
    connection.close()


def update(my_id, salary):
    connection = psycopg2.connect(dbname='database1', user='udit', password='udit1234', host='localhost')
    cursor = connection.cursor()
    cursor.execute("UPDATE my_table SET salary = %s WHERE id = %s", (salary, my_id))
    connection.commit()
    connection.close()


create_table()
insert('2', 'udit2', '1002')
delete('2')
update('1', 1000)
print(select())
