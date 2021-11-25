# Object and Attributes

# print out attributes of int except magic ones (__X_)


def foo(some_class):
    op = []
    for x in dir(some_class):
        if x.startswith('__'):
            print("starting with __", x)
        else:
            op.append(x)
    return op


def goo(some_class):
    return [x for x in dir(some_class) if not x.startswith('__')]


print(goo(int))
print(foo(str))

import re


def foo(obj):
    all_attributes = dir(obj)
    normal_attributes = [attribute \
                         for attribute in all_attributes \
                         if not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
    return normal_attributes
