# function that takes infinite number of lists and return concatenated list

def foo(*args):
    list_ = []
    for arg in args:
        list_ = list_ + arg
    return list_


print(foo([1, 2], [2, 3, 4], [33, 44]))
