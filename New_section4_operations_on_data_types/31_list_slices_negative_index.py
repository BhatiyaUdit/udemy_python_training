
# list indexes
#        0  1  2  3  4  5
list_ = [1, 2, 3, 4, 5, 6]
#       -6 -5 -4 -3 -2 -1


# always remember when upper limit is specified then it includes till upper_limit -1

# print whole list
print(list_[:])

# print last two items
sublist_1_4 = list_[-2:]
print(sublist_1_4)

# print list from fourth last to second last
sublist = list_[-4: -1]
print(sublist)


# print list from start to third last item
sublist = list_[: -2]
print(sublist)
