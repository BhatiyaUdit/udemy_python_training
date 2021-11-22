# waf input = string
# output = True if string contains "xxx" else false


def foo(string):
    return True if 'xxx' in string else False


print(foo("xxx"))