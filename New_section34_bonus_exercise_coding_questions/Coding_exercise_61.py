# function to return first and last item of the list passed


def foo(list_: list):
    if list_:
        first = list_[0]
        last = list_[-1]
        return first, last


print(foo([1, 2, 3]))
