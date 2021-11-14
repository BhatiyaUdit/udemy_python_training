def func(*args):
    print(args)
    print(type(args))
    return args


print(func(11, 2, 3, 4, 5, 6, 8))

# args will be converted to tuple type and we can perform all operations on it
