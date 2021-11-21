# function that takes infinite number of lists
# and returns true if all lists have at least one item else False

def foo(*args):
    result = True
    for arg in args:
        if not arg:
            result = False
            break
    return result


def foo2(*args):
    return all(args)


print(foo2([1, 2], [2, 3, 4], [33, 44], []))
