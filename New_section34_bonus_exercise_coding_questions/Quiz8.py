# function to return concot of three lists

def foo(*args):
    print(type(args))
    return args * 2


print(foo([1, 2], [2], [33]))
