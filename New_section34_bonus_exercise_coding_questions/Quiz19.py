# Mutability

"""
What is output?

"""

a = 3
b = 3

c = [1, 2]
d = [1, 2]

print(a is b)
print(c is d)

# answer True, False
# because [1,2] is different reference


#
# Correct! Integers (e..g 3) are immutable objects. Lists (e.g. [1, 2]) are mutable.
# Since an integer is immutable (cannot be modified) then only one instance is kept in memory
# no matter how many references there are (e.g. a and b).
# Therefore, integer referenced by a is the same one referenced by b.
# Whereas, since lists are mutable (e.g. you can remove an item from an existing list)
# each list is stored as a separate object. Therefore, the one stored in c is different than the one stored in d.
#
# #
