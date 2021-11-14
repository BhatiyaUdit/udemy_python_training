# create a function that takes a list with numbers and returns list with +ve numbers only
def return_number_list(data):
    return [value for value in data if value > 0]


print(return_number_list([1, 2, 3, -9, 5]))
