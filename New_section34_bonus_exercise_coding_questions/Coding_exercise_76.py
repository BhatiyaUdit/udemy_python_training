# function that takes list as param and returns a list that have
# every 7th element of the original list

def foo(lst):
    new_lst = []
    for x in range(0, len(lst), 7):
        new_lst.append(lst[x])
    return new_lst


print(foo([2, 19, 99, 101, 2, 3, 4, 5]))


# instructor solution
def foo(mylist):
    return mylist[::7]


print(foo([2, 19, 99, 101, 2, 3, 4, 5]))