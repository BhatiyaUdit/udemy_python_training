# waf input = list with duplicates
# output = list without duplicates

def foo(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list = new_list + [item]
    return new_list


print(foo([5, 8, 9, 10, 10]))


def foo(mylist):
    return list(set(mylist))


print(foo([5, 8, 9, 10, 10]))
