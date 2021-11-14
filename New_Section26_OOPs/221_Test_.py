# If you want to import something from python file then it should not start with number

# from file import class
# when we call the constructor the instance of the class is sent to constructor
# in below example variable d will be received in self
# therefore we should always have self :: as a convention :: as param in init method to make the code work

# the methods of the class also takes the instance as the parameter and raises exception if self is not
# provided in method declaration

# to pass other parameters we need to pass them after the instance (self)

from Using_oops_in_program_221 import Demo

d = Demo()
d.create_table()
print(d.view())
a = Demo()