# Better array memory

"""
which of the following will consume less memory

"""

numbers = list(range(1, 10))

for number in numbers:
    print(number)

# ----- option 2 ----
import array

numbers = array.array('i', range(1, 10))

for number in numbers:
    print(number)

# option 1 or 2
# ans option 2


# A list can contain a mix of different datatypes.
# An array can only contain homogenous items.
# This makes an array occupy less size than a list.
# Therefore, an array is a better choice when dealing with big arrays
# of homogenous items (e.g. only numbers, only strings, etc.)
# #
