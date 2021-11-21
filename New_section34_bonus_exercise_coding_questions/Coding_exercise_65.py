# pass n arguments and returns as a list

def foo(*args):
    return list(args)


print(foo(1, 3, 5))
