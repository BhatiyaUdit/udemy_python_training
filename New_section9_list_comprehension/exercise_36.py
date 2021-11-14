# create a function that takes a list with strings and numbers and returns list with numbers only
def return_number_list(data):
    return [value for value in data if type(value) == int]


print(return_number_list([1,2,3,'dd',5]))