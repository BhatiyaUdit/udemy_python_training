def func(**args):
    print(args)
    print(type(args))
    return args


print(func(a=2, b=3, c=4, d=5, e=6, f=8))

# all args must be key args
# args will be converted to dict type and we can perform all operations on it


