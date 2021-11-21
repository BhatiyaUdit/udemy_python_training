# function to return first item of the list passed


def foo(list_: list):
    return list_[0] if list_ else None


print(foo([1, 2, 3]))
