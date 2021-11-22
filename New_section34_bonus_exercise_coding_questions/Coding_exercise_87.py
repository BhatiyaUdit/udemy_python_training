# waf input = dictionary of lists {a : [10, 20], b : [1] ,...}
# output = sum of values of all keys


def foo(dictt):
    print(dictt.values())
    print(type(dictt.values()))
    #return sum(dictt.values())
    sum_ = 0
    for value in dictt.values():
        sum_ = sum_ + sum(value)
    return sum_


print(foo({'a': [10, 20], 'b': [1]}))


def foo2(dictt):
    return sum([sum(value) for value in dictt.values()])


print(foo2({'a': [10, 20], 'b': [1]}))
