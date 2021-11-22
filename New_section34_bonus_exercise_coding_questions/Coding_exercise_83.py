# waf input =
# output = list of 1000 random integers
# integers should be between 1 to 10 inclusive
import random


def foo():
    lst = []
    for i in range(0, 100):
        lst.append(random.randint(1, 10))
    return lst


print(foo())

import random


def foo():
    return [random.randint(1, 10) for i in range(1000)]
