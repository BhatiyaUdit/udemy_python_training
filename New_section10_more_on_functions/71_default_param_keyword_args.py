# default param functions

# NOTE : default params must always be after non-default params

def func(a, b=1):
    print(a, b)
    return a


print(func(3))
print(func(4, 5))


# Keyword args function call

def func(a, b):
    print(a, b)
    return a


print(func(a=4, b=9))
print(func(b=3, a=5))


# Non Keyword args function call

def func(a, b):
    print(a, b)
    return a


print(func(4, 9))
print(func(3, 5))
