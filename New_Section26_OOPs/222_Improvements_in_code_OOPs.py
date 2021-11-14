"""
Improvement 1 : Create the connection in init method
                Keep the connection open
                Pass the reference of the same object to other functions
                ReUse connection object instead of creating it multiple times

Steps :
    Put create code in init
    Remove Close connection from there
    Remove open connection from other methods
    Try to execute : Error 1 : no Cursor object defined as cursor variable is not in method scope
                                Fix : Try to access using self
                     Error 2 : Database object does not have cursor variable
                                Fix : Try to put the cursor in self in init itself
                                        Cur will become the attribute of the class
    Put Connection object into self also to commit the db changes done during method execution

For activities like closing connection and other clean up
we have destructor method __del__(self)

"""

from Using_oops_in_program_improv_222 import Demo

database = Demo()
data = database.view()
print(data)
database.insert(2, 'ancd', 1222)
data = database.view()
print(data)
