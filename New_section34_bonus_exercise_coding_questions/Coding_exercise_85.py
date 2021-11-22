# waf input = list of objects
# output = all items that contain "xxx"


def foo(lst):
    return [item for item in lst if type(item) == str and "xxx" in item]


print(foo("xxx"))


def foo(mylist):
    return [string for string in mylist if isinstance(string, str) and "xxx" in string]
