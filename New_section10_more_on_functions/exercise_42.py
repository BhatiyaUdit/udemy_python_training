# Take n number of argument
# return list
# all strings in the list should be converted to upper case
# list items should be sorted alphabetically


def foo(*args):
    list_data = list(args)
    list_data = [data.upper() for data in list_data]
    list_data.sort()
    return list_data


print(foo("hi", 'bye'))


# alternative
def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)
