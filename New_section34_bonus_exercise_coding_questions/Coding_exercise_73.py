# function that takes list as param and returns last element
# string "Empty List" if the list does not have elements


def foo(lst):
    return lst[-1] if lst else "Empty List"


print(foo([]))
