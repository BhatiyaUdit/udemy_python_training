# waf to return middle item of odd numbered list


def foo(lst):
    middle = (len(lst)) / 2
    return lst[int(middle)]


print(foo([5, 8, 9]))
