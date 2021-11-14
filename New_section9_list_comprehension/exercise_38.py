# create a function that takes a list with strings and numbers and returns list with numbers only
# replace string with 0

def return_number_list(data):
    return [value if type(value) == int else 0 for value in data]


print(return_number_list([1, 2, 3, 'dd', 5]))
