# function that returns another function

def foo():
    return "Hello"


def foo_ret():
    return foo


l = foo_ret()
print(l, type(l))
print(l())