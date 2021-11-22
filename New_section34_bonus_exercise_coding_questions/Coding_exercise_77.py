# function that takes list as param and returns a list that have
# 5 elements at every 7th step

# ex [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# op = [1,2,3,4,5 , 8,9,10,11,12,  15]

def foo(lst):
    new_lst = []
    for x in range(0, len(lst), 7):
        new_lst = new_lst + lst[x:x + 5]
    return new_lst


print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

# instructor solution
import itertools


def foo(mylist):
    list_of_lists = [mylist[i:i + 5] for i in range(0, len(mylist), 7)]
    print(list_of_lists)
    return list(itertools.chain.from_iterable(list_of_lists))


print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
