# waf input = dictionary
# output = sum of values of all keys


def foo(dictt):
    print(dictt.values())
    return sum(dictt.values())


print(foo({'a': 1, 'b': 2}))
