# Better Sum

"""
which of the following will be considered better

"""

numbers = range(1000000)

# option 1
print(sum(number for number in numbers if number > 2))

# option 2
print(sum([number for number in numbers if number > 2]))

# option 1 or 2
# ans option 1  does not create extra list


# This code is better because it doesn't create a list object like the other alternative does.
# This uses a generator. The expression "(number for number in numbers if number &gt; 2)" is a generator.
# It does things one step at a time without using a large object such as a list. This is good for memory.
# ##
