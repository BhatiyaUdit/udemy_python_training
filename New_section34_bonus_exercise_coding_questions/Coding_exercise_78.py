# function that takes list as param and returns a list that have
# X number of elements at every yth step

# ex [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# op = [1,2,3,4,5 , 8,9,10,11,12,  15]

def foo(lst, n, y):
    new_lst = []
    for x in range(0, len(lst), y):
        new_lst = new_lst + lst[x:x + n]
    return new_lst


print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3, 7))

# instructor solution
import itertools


def foo(mylist, x, y):
    list_of_lists = [mylist[i:i + x] for i in range(0, len(mylist), y)]
    print(list_of_lists)
    return list(itertools.chain.from_iterable(list_of_lists))


print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1, 2))
