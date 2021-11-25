# Better memory

"""
which of the following will consume less memory

"""


a = 1000000 * 'a'
b = 1000000 * 'b'

with open("./files10/sample1.txt", 'w') as file1:
    file1.write(a+b)

with open("./files10/sample2.txt", 'w') as file2:
    file2.write(a)
    file2.write(b)



# option 1 or 2
# ans option 2 it will aviod creating another object a+b in memory before storage


# Correct! This code is better because it avoids the construction of the a + b string.
# Since a and b are already big, a + b would be even bigger so you want to avoid storing such large strings in memory,
# It it's too big you could even get a MemoryError. In case of memory errors you need to figure out a way
# to split your big objects into smaller objects.
# #

