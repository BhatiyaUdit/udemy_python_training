# function that takes list as param and returns a list that have
# all the elements except the first one if list length is 3
# else None

def foo(lst, obj):
    new_lst = None
    if len(lst) >= 3:
        new_lst = lst[1:] + [obj]
    return new_lst


print(foo([2, 19, 99, 101], 555))


# instructor solution
def foo(lst, item):
    if len(lst) == 3:
        lst.pop(0)
        lst.append(item)
        return lst
