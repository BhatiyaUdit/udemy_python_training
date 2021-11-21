# pass args for below output
# [2,6,10]

def foo(*args):
    return [x * 2 for x in args]


print(foo(1, 3, 5))
