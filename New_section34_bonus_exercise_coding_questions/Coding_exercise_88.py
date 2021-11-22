# waf input = dictionary
# output = dictionary with keys that have value > 4


def foo(dictt):
    new_dict = {}
    for item in dictt.items():
        if item[1] > 4:
            new_dict[item[0]] = item[1]
    return new_dict


print(foo({'a': 1, 'b': 5}))


def foo(mydict):
    return dict((key, value) for key, value in mydict.items() if value > 4)
