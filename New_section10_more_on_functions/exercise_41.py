# return avg by accepting n number of args

def foo(*args):
    return sum(args) / len(args)


print(foo(10, 20, 30, 40))
